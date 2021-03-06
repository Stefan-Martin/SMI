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
    We use the min or max depending on direction of acceleration.

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

def segment_signal(signal: np.array, peaks: np.array, vallies: np.array):
    """Segment the SMI signal into important regions.

    To perform phase unwrapping, we need to know when we are inbetween a valley
    and a peak, inbetween a peak and a valley, and when we are in a area of
    reversal. Step through the signal in O(n_peaks) time and perform this
    segmentation. This is a highly crunchy function.

    Args:
        signal (np.array): SMI Signal
        peaks (np.array): peak locations in |signal|.
        vallies (np.array): valley locations in |signal|.

    Returns:
        np.array, np.array, np.array: arrays indicating
            when we are in a V-P, P-V or reversal segment, respectively. P-V
            and V-P arrays are binary, and the reversal array uses 1 or -1 to
            indicate sign of direction change."""

    peak_valley = np.zeros_like(signal)
    valley_peak = np.zeros_like(signal)
    reversal = np.zeros_like(signal)

    current = None
    peak_index = 0
    valley_index = 0
    # check where we start on the first fringe
    # we start between a valley and a peak
    if peaks[0] < vallies[0]:
        valley_peak[0:peaks[0]] = 1
        current = 'p'
    # we start between a peak and a valley
    else:
        peak_valley[0:vallies[0]] = 1
        current = 'v'


    done = False
    while not done:

        # if we are currently at a peak
        if current == 'p':

            # if no more peaks to go to but still at least 1 valley
            if (peak_index == len(peaks) - 1) and (valley_index <= len(vallies) -1):
                peak_valley[peaks[peak_index]:vallies[valley_index]] = 1
                current = 'v'
                peak_index += 1

            # if no more vallies to go to
            elif valley_index > len(vallies) - 1:
                # we must be at the end of the signal and be in a P-V reigon
                peak_valley[peaks[peak_index]:] = 1
                done = True

            else:
                current_peak = peaks[peak_index]
                next_peak = peaks[peak_index + 1]
                next_valley = vallies[valley_index]

                # if next valley closer than next peak
                if (next_valley - current_peak) < (next_peak - current_peak):
                    peak_valley[current_peak:next_valley] = 1
                    current = 'v'
                    peak_index += 1

                else: # if next peak is closer we are in a reversal
                    reversal[current_peak:next_peak] = 1
                    peak_index += 1

        # we are currently at a valley
        else:

            # if no more vallies to go to but still at least 1 peak
            if (valley_index == len(vallies) - 1) and (
                    peak_index <= len(peaks) - 1):
                valley_peak[vallies[valley_index]:peaks[peak_index]] = 1
                current = 'p'
                valley_index += 1

            # if no more peaks to go to
            elif peak_index > len(peaks) - 1:
                # we must be at the end of the signal and be in a V-P reigon
                valley_peak[vallies[valley_index]:] = 1
                done = True
            else:
                current_valley = vallies[valley_index]
                next_valley = vallies[valley_index + 1]
                next_peak = peaks[peak_index]

                # if next peak closer than next valley
                if (next_peak - current_valley) < (next_valley - current_valley):
                    valley_peak[current_valley:next_peak] = 1
                    current = 'p'
                    valley_index += 1

                else:  # if next peak is closer we are in a reversal
                    reversal[current_valley:next_valley] = 1
                    valley_index += 1

    return peak_valley, valley_peak, reversal

def unwrap_phase(signal: np.array,
                 direction: np.array,
                 p_v_segments: np.array,
                 v_p_segments: np.array,
                 reversal_segments: np.array,
                 vallies: np.array):
    """Apply the phase unwrapping algorithm.

    Unwrap the phase of the SMI signal using previously extracted information
    about movement direction, peak location, valley location, and jumping point
    location. Follows the work of:
    https://sci-hub.tw/https://www.osapublishing.org/ao/abstract.cfm?uri=ao-50-26-5064

    Args:
        signal (np.array): NORMALIZED SMI signal.
        direction (np.array): extracted movement direction at every point in
            |signal|.
        p_v_segments (np.array): array parralel to |signal| that contains a 1 if
            this part of signal is in located inbetween a peak and a valley
            (0 otherwise).
        v_p_segments (np.array): array parralel to |signal| that contains a 1 if
            this part of signal is in located inbetween a valley and a peak
            (0 otherwise).
        reversal_segments (np.array): array parralel to |signal| that contains
            a 1 if this part of signal is in an area of a v-v reversal and a
            -1 if this part of the signal is in an area of a p-p reversal.
    Returns:
        np.array: unwrapped phase
        """

    # construct phase discontinuity array
    phase_disc = np.zeros_like(signal)
    running_sum = 0
    for index,_ in enumerate(signal):
        if index in vallies:
            running_sum += (2 *np.pi) * -1 * direction[index]
        phase_disc[index] = running_sum


    # construct wrapped phase array
    wrapped_phase = np.arccos(signal)

    # construct unwrapped phase array
    unwrapped_phase = np.zeros_like(signal)

    # v-p segments
    unwrapped_phase += np.multiply(np.multiply(wrapped_phase,direction), v_p_segments)

    # p-v segments
    unwrapped_phase += np.multiply(np.multiply(wrapped_phase, -1 * direction), p_v_segments)

    # reversal segments
    unwrapped_phase += np.multiply(-1*wrapped_phase, reversal_segments)

    # phase discontinuity
    unwrapped_phase += phase_disc

    return unwrapped_phase

def remove_feedback_dynamics(unwrapped_phase: np.array,
                             C: numbers.Real,
                             alpha: numbers.Real):
    """Invert the feedback dynamics according to the Lang-Kobyashi equations.

    Recover the actual accumulated phase by inverting equation 2 from
    https://sci-hub.tw/https://www.osapublishing.org/ao/abstract.cfm?uri=ao-50-26-5064

    Args:
        unwrapped_phase (np.array): unwrapped phase (referenced to actual laser
            wavelength)
        C (numbers.Real): ackett's coupling factor for this signal
        alpha (numbers.Real): Linewidth enhancement factor for this signal

    Returns:
        np.array: nominal accumulated phase
    """
    nominal_phase = unwrapped_phase + C * np.sin(unwrapped_phase + np.arctan(alpha))
    return nominal_phase





input_displacement_path = os.path.join(os.getenv('HOME'),'interferometry_data/15SNR_in.csv')
smi_signal_path = os.path.join(os.getenv('HOME'),'interferometry_data/15SNR_out.csv')

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

pr, vr, rr = segment_signal(signal=smi_signal, vallies=v, peaks=p)

unwrapped_phase = unwrap_phase(signal=smi_signal,
                               direction=direction,
                               p_v_segments=pr,
                               v_p_segments=vr,
                               reversal_segments=rr,
                               vallies=v)

nominal_phase = remove_feedback_dynamics(unwrapped_phase, C=3, alpha=6)

error = (input_diplacement - np.mean(input_diplacement)) - (nominal_phase - np.mean(nominal_phase))


# plotting
matplotlib.rcParams['figure.dpi'] = 300
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, figsize=(8, 8))
ax1.plot(input_diplacement, linewidth=1)
ax1.set_ylabel('Input Displacement (x/λ)')
ax2.plot(smi_signal, linewidth = 1)
ax2.set_ylabel('SMI Signal (V)')
for item in p:
    ax2.axvline(x=item, color = 'r', linewidth = 0.5)
for item in v:
    ax2.axvline(x=item, color = 'g', linewidth = 0.5)
ax3.plot(unwrapped_phase, linewidth=1)
ax3.set_ylabel('Recovered Feedback \n Phase (rad)')
ax4.plot(nominal_phase, linewidth=1)
ax4.set_ylabel('Recovered \n Displacement (x/λ)')
ax5.plot(error, linewidth=0.5)
ax5.set_ylabel('Error (x/λ)')
ax5.set_xlabel('Sample')
fig.suptitle('The Improved Phase Unwrapping Method (C=3, α=6)')
limits = [0,10000]
ax1.set_xlim(limits)
ax2.set_xlim(limits)
ax3.set_xlim(limits)
ax4.set_xlim(limits)
ax5.set_xlim(limits)
ax5.set_ylim([-0.003,0.003])
plt.savefig(os.path.join(os.getenv('HOME'),'interferometry_data/15SNRplot.png'))

