from scripts import step_detect
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
#import cv2

def find_inflections_above_under(signal, low_threshold, high_threshold, group_threshold = 50):

    def find_max_in_sequences(array):
        sequences = []
        prev = -200
        for element in array:
            if element < prev + group_threshold:
                sequences[-1].append(element)
            else:
                sequences.append([element])
            prev = element
        maxs = []
        for seq in sequences:
            maxs.append(max(seq))
        return maxs

    above_infl = find_max_in_sequences(np.argwhere(signal > high_threshold).flatten())
    below_infl = find_max_in_sequences(np.argwhere(signal < low_threshold).flatten())

    return above_infl, below_infl


def jump_magnitude_threshold(candidate_fringes,smi_signal,jump_threshold=0.08,window_scale=20):
    fringes=[]
    window_size=int(window_scale*np.ceil(sampling_rate/100000))
    center=window_size
    for i in candidate_fringes:
        window=smi_signal[i-window_size:i+window_size]
        extrema = np.sign(np.diff(window))
        extrema[2 * window_size-2] = 1
        for j,k in enumerate (extrema):
            if extrema[j] == 0:
                extrema[j]=extrema[j-1] #to avoid treating zero as a sign change we hold the prior value of the derivative
        extrema=np.diff(extrema).nonzero()[0]+1 #find all the derivative sign changes, these are all local extrema
        peaks_below=extrema[extrema < center]
        peaks_above=extrema[extrema >center]
        if len(peaks_above)==0 or len(peaks_below)==0: #not a real discontinuity since no extrema above or below
            continue
        a=peaks_below.max() #index of first peak below
        b=peaks_above.min()  # index of first peak above
        #plt.plot(window, '-rD', markevery=[a,b]) #show each fringe
        #plt.show()
        if abs(window[a]-window[b])>jump_threshold*np.std(smi_signal):
            fringes.append(i)
    return fringes

std_threshold = 2.5
sampling_rate = 300000
wavelength=639
process_time_bounds = [5, 9.1]

full_signal=np.load('/home/stefan/smi_data/target_on.npy').flatten()/(2 ** 12)

reduced_signal = full_signal[int(process_time_bounds[0]* sampling_rate):int(process_time_bounds[1] * sampling_rate)]
times = np.array(list(range(len(reduced_signal))))/sampling_rate + process_time_bounds[0]

filtered_signal = signal.medfilt(reduced_signal, 11)#cv2.bilateralFilter(np.array(reduced_signal, dtype=np.float32),11, 150, 150).flatten()

mz_steps = step_detect.mz_fwt(filtered_signal, n=5)

mz_std = np.std(mz_steps)
mz_mean = np.mean(mz_steps)
pos_fringes, neg_fringes = find_inflections_above_under(mz_steps, mz_mean - (std_threshold * mz_std), mz_mean + (std_threshold * mz_std))


pos_fringes=jump_magnitude_threshold(pos_fringes,filtered_signal)
neg_fringes=jump_magnitude_threshold(neg_fringes,filtered_signal)

filtered_gradient = np.gradient(filtered_signal, axis=0)
mean_grad = np.mean(filtered_gradient)
std_grad = np.std(filtered_gradient)

possible_fringe_indicies= np.argwhere(np.abs(filtered_gradient - mean_grad) > std_threshold * std_grad).flatten()

plot, axs = plt.subplots(nrows=3, ncols=1)
max_sig = np.max(filtered_signal)
min_sig = np.min(filtered_signal)
axs[0].plot(times, filtered_signal, linewidth = 0.2, color='r')
for fr in pos_fringes:
    axs[0].plot([times[fr], times[fr]], [min_sig, max_sig], color='orange')
for fr in neg_fringes:
    axs[0].plot([times[fr], times[fr]], [min_sig, max_sig], color='blue')
min_sig = np.min(filtered_signal)
max_sig = np.max(filtered_signal)


axs[2].plot(times, filtered_gradient, linewidth = 0.5, color='r')
axs[2].plot(process_time_bounds, [mean_grad + std_threshold * std_grad,mean_grad + std_threshold * std_grad], label = r'$\pm 3 \sigma$', linewidth=1, color='g')
axs[2].plot(process_time_bounds, [mean_grad - std_threshold * std_grad,mean_grad - std_threshold * std_grad], linewidth=1, color='g')

axs[1].plot(times, mz_steps, color='r')
axs[1].plot(process_time_bounds, [mz_mean + std_threshold * mz_std,mz_mean + std_threshold * mz_std], label = r'$\pm 3 \sigma$', linewidth=1, color='g')
axs[1].plot(process_time_bounds, [mz_mean - std_threshold * mz_std,mz_mean - std_threshold * mz_std], linewidth=1, color='g')

axs[0].set_ylabel('Voltagae (V)')
axs[2].set_ylabel(r'$ \frac{dV}{dt}$(V/s)')
axs[1].set_ylabel('Multiscale Edges')
#axs[1].set_yscale('log')
axs[2].set_xlabel('time (s)')

net_fringes=len(pos_fringes) - len(neg_fringes)
axs[0].set_title('Net travel: {} um'.format(wavelength*net_fringes/1000*0.5))

plot.show()

print("")


