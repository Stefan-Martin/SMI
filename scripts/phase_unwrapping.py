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
                           jump_points: np.array):
    """Find the peaks and valleys in the SMI signal.

    A peak is the argmax of the SMI signal between two jump points, and a valley
    is the argmin of the SMI signal between peaks.

    Args:
        signal (np.array): NORMALIZED SMI signal
        jump_points (np.array): Jump points found in signal.
        jump_signs (np.array): Array parralel to jump_points representing
            direction of each jump.

    Returns:
        np.array, np.array: Arrays containing peaks and valleys, respectively
    """
    aug_jump_points = [0] + list(jump_points) + [len(signal)]
    # peak finding
    peaks = []
    last = aug_jump_points[0]
    for point in aug_jump_points[1:]:
        relevant_window = signal[last:point]
        max_point = np.argmax(relevant_window)
        actual_index = last + max_point
        # if the maximum value occurs first or last in the signal we can't be
        # sure its a peak
        if not (actual_index == 0 or actual_index == len(relevant_window) - 1):
            peaks.append(actual_index)
        last = point

    # valley finding
    vallies = []
    last = aug_jump_points[0]
    for point in aug_jump_points[1:]:
        relevant_window = signal[last:point]
        min_point = np.argmin(relevant_window)
        actual_index = last + min_point
        # if the maximum value occurs first or last in the signal we can't be
        # sure its a peak
        if not (actual_index == 0 or actual_index == len(relevant_window) - 1):
            vallies.append(actual_index)
        last = point

    return np.array(peaks), np.array(vallies)




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

def find_wrapped_phase(signal: np.array):
    """Find the wrapped phase from the normalized SMI signal.

    We find the unwrapped phase by applying the inverse cosine function to the
    normalized SMI signal. Note that this is only possible if the signal is
    normalized due to the domain of the arccos function.

    Args:
        signal (np.array): NORMALIZED SMI signal

    Returns:
        np.array: array same size of signal representing wrapped phase
    """
    return np.arccos(signal)

def unwrap_phase(wrapped_phase: np.array, ):
    pass




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
                              jump_points=jump_points)

first_diff = np.diff(smi_signal)


matplotlib.rcParams['figure.dpi'] = 200
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=(8, 3))
ax1.plot(smi_signal)
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
a = np.std(first_diff)
plt.tight_layout()
plt.show()

print("")