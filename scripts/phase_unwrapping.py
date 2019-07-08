import os
import numbers
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def find_jump_points(signal: np.array, thresh_std: float = 3):
    """Find the jump points in the smi signal.

    Here we assume jump points are points with abnormally large first
    derivatives.

    Args:
        signal (np.array): NORMALIZED SMI signal
        thresh_std (numbers.Real): threshold in number of standard deviations
            above zero to apply to differentiated signal in finding jump points

    Returns:
        np.array, np.array, np.array: arrays containing -
            1. Signed pulse train representing the jumps, same size as signal
            2. Array of jump locations
            3. Array of jump signs
    """
    first_diff = np.diff(signal)
    abs_first_diff = np.absolute(first_diff)
    std = np.std(first_diff)
    pulse_train = np.zeros_like(signal)
    start = None
    jump_points = []
    jump_signs = []
    for index,item in enumerate(abs_first_diff):
        if item > thresh_std * std:
            if start is None:
                start = index
        else:
            if start is not None:
                jump_point = start + np.argmax(abs_first_diff[start:index+1])
                jump_sign = np.sign(first_diff[jump_point])
                jump_points.append(jump_point)
                jump_signs.append(jump_sign)
                pulse_train[jump_point] = 1 * jump_sign
                start = None
    return pulse_train, np.array(jump_points), np.array(jump_signs)


def find_peaks_and_valleys(signal: np.array,
                           jump_points: np.array,
                           turnaround_points: np.array,
                           direction: np.array):
    """Find the peaks and valleys in the SMI signal.

    A peak is the argmax of the SMI signal between two jump points, and a valley
    is the argmin of the SMI signal between peaks. Also must handle edge cases
    near turnaround points.

    Args:
        signal (np.array): NORMALIZED SMI signal
        jump_points (np.array): Jump points found in signal.
        jump_signs (np.array): Array parralel to jump_points representing
            direction of each jump.

    Returns:
        np.array, np.array: Arrays containing peaks and valleys, respectively
    """
    aug_jump_points = [0] + list(jump_points)

    peaks = []
    vallies = []
    turnaround_counter = 0

    for index,current in enumerate(aug_jump_points[:-1]):
        next = aug_jump_points[index+1]
        if not turnaround_points.size:
            current_turnaround = -1
        else:
            current_turnaround = turnaround_points[turnaround_counter]

        # if current_turnaround closer than next jump
        if (current_turnaround - current) > 0 and (np.abs(current_turnaround - current) < np.abs(next - current)):

            # if moving towards laser after turnaround
            if (direction[current] == -1) and (direction[next] == 1):

                # look for valley between current and turnaround
                vallies.append(
                    current + np.argmin(signal[current:current_turnaround])
                )

                # look for valley between turnaround and next
                vallies.append(
                    current_turnaround + np.argmin(
                        signal[current_turnaround:next+1]
                    )
                )

            # if moving away from laser after turnaround
            else:

                # look for a peak between current and turnaround
                peaks.append(
                    current + np.argmax(signal[current:current_turnaround])
                )

                # look for a peak between turnaround and next
                peaks.append(
                    current_turnaround + np.argmax(
                        signal[current_turnaround:next]
                    )
                )
            if turnaround_counter < len(turnaround_points)-1:
                turnaround_counter += 1
        else:
            this_peak = current + np.argmax(signal[current:next])
            if not this_peak == 0 or this_peak == len(signal)-1:
                peaks.append(this_peak)

    # find the rest of the vallies in-between peaks. Do this seperately because
    # vallies are typically very close to jump points which makes finding them
    # between jump points un-reliable
    aug_peaks = peaks + [len(signal)]
    for index,current in enumerate(aug_peaks[:-1]):
        next = aug_peaks[index + 1]
        # if there is a turnaround between current and next do not look for a
        # valley
        for turn in turnaround_points:
            if current<turn<next:
                break
        else:
            this_valley = current + np.argmin(signal[current:next])
            if not (this_valley == 0 or this_valley == len(signal)-1):
                vallies.append(this_valley)

    return np.array(sorted(peaks)), np.array(sorted(vallies))




def find_points_of_reversal(signal: np.array,
                            jump_points: np.array,
                            jump_signs: np.array,
                            buffer: int = 10):
    """Reversal points are where we think the target has changed directions.

    Reversal points are located in-between jump points of opposite signs.
    We use the min or max (dependant on second derivative of signal in region
    of reversal.

    Args:
        signal (np.array): NORMALIZED SMI signal
        jump_points (np.array): Jump points found in signal.
        jump_signs (np.array): Array parralel to jump_points representing
            direction of each jump.
        buffer (int): buffer size to use when locating max/min point in
            reversal region (to avoid triggering on jump).

    Return:
        np.array: Array containing indicies of reversal points
    """
    reversal_points = []
    for index, _ in enumerate(jump_points[0:len(jump_points)-1]):

        # if we are in a region of reversal
        lhs_point = jump_points[index] + buffer
        rhs_point = jump_points[index+1] - buffer
        if not (jump_signs[index] * jump_signs[index + 1] == 1):
            if jump_signs[index] < 0:
                reversal_points.append(
                    lhs_point + np.argmax(
                        signal[lhs_point:rhs_point+1]
                    )
                )
            else:
                reversal_points.append(
                    lhs_point + np.argmin(
                        signal[lhs_point:rhs_point + 1]
                    )
                )
    return np.array(reversal_points)


def find_motion_direction(jump_pulse_train: np.array,
                          reversal_points: np.array):
    """Determine which direction the target was moving.

    Determine motion direction by looking at jump signs in-between points of
    reversal.

    Args:
        jump_pulse_train (np.array): pulse train representing jump location
            and direction
        reversal_points (np.array): array containing indicies of reversal points

    Returns:
        np.array: array the same size as the SMI signal containing a 1 for
            movement towards the laser source and a -1 for movement away from the
            laser source
        """

    # simplify the logic by adding zero and len of
    # signal to reversal point array
    aug_reversal_points = np.array(
        [0] + list(reversal_points) + [len(jump_pulse_train)]
    )

    direction = np.zeros_like(jump_pulse_train)

    # all direction changes in middle
    last = aug_reversal_points[0]
    for item in aug_reversal_points:
        this_direction = np.mean(jump_pulse_train[last:item])
        direction[last:item] = 1 * np.sign(this_direction)
        last = item

    return direction


def unwrap_phase(signal: np.array,
                 direction: np.array,
                 peaks: np.array,
                 vallies: np.array,
                 jump_points: np.array):
    """Apply the phase unwrapping algorithm.

    Unwrap the phase of the SMI signal using previously extracted information
    about movement direction, peak location, valley location, and jumping point
    location.

    Args:
        signal (np.array): NORMALIZED SMI signal.
        direction (np.array): extracted movement direction at every point in
            |signal|.
        peaks (np.array): peak locations in |signal|.
        vallies (np.array): valley locations in |signal|.
        jump_points (np.array): jump locations in |signal|.

    Returns:
        np.array: unwrapped phase
        """
    unwrapped_phase = np.zeros_like(signal)
    wrapped_phase = np.arccos(signal)
    i_v = 0
    i_j = 0
    i_vp = 1
    if np.sign(signal[1] - signal[0]) == \
            np.sign(wrapped_phase[1] - wrapped_phase[0]):
        i_vp = 0
    for index, (this_direction, this_wrapped) in enumerate(zip(direction, wrapped_phase)):
        if (index in peaks) or (index in vallies):
            i_vp += 1
        if (index in vallies) and this_direction == 1:
            i_v -= 1
        if (index in vallies) and this_direction == -1:
            i_v += 1
        if (index in jump_points) and this_direction == -1:
            i_j += 1

        if this_direction == -1:

            # check if in-between peak and jump
            # (is closest point on right a jump?)
            rhs_peaks = peaks[peaks > index]
            rhs_jumps = jump_points[jump_points > index]

            # case 0: in-between peak and jump
            # case 1: in-between valley and peak
            if rhs_jumps.size and not rhs_peaks.size:
                case = 0
            elif rhs_peaks.size and not rhs_jumps.size:
                case = 1
            elif not rhs_peaks.size and not rhs_jumps.size:
                case = 1
            else:
                closest_rhs_jump = np.min(rhs_jumps - index)
                closest_rhs_peak = np.min(rhs_peaks - index)
                if(closest_rhs_jump - index) < (closest_rhs_peak - index):
                    case = 0
                else:
                    case = 1

            if case:
                unwrapped_phase[index] = (-1*this_wrapped) + 2*np.pi*i_v
            else:
                unwrapped_phase[index] = this_wrapped + 2*np.pi*i_j

        else:
            unwrapped_phase[index] = (((-1) ** (i_vp)) * this_wrapped) + 2*np.pi*(i_v + 1)

    return unwrapped_phase






input_displacement_path = os.path.join(os.getenv('HOME'),'interferometry_data/30_in.csv')
smi_signal_path = os.path.join(os.getenv('HOME'),'interferometry_data/30_out.csv')

input_diplacement = np.genfromtxt(input_displacement_path, delimiter=',')[:10000]
smi_signal = np.genfromtxt(smi_signal_path, delimiter=',')[:10000]

jump_pulse_train, jump_points, jump_signs = find_jump_points(smi_signal)

rev_ponts = find_points_of_reversal(signal=smi_signal,
                                    jump_points=jump_points,
                                    jump_signs=jump_signs)

direction = find_motion_direction(jump_pulse_train=jump_pulse_train,
                      reversal_points=rev_ponts)

p, v = find_peaks_and_valleys(signal=smi_signal,
                              jump_points=jump_points,
                              turnaround_points=rev_ponts,
                              direction=direction)

unwrapped_phase = unwrap_phase(signal=smi_signal,
                               direction=direction,
                               peaks=p,
                               vallies=v,
                               jump_points=jump_points)

matplotlib.rcParams['figure.dpi'] = 200
fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, figsize=(8, 3))
ax1.plot(smi_signal, linewidth = 0.5)
ax1.set_ylabel('Normalized SMI \n Signal')
for item in p:
    ax1.axvline(x=item, color = 'r', linewidth = 0.5)
for item in v:
    ax1.axvline(x=item, color = 'g', linewidth = 0.5)
ax2.plot(direction)
ax2.set_ylabel('Motion Direction')
ax3.plot(jump_pulse_train)
ax3.set_ylabel('Jump Points')
ax4.plot(input_diplacement)
ax4.set_ylabel('Input')
ax5.plot(unwrapped_phase)
ax5.set_ylabel('UWP')
ax6.plot(np.arccos(smi_signal))
plt.tight_layout()
plt.show()

print("")