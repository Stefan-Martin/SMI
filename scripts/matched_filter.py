import numpy as np
import pywt
import matplotlib.pyplot as plt
from scipy import signal

sampling_rate = 300000
mother_wavelet_bounds = [5.36,5.46]

full_signal=np.load('/home/trevor/smi_data/stage_emi_test/target_on.npy').flatten()/(2 ** 12)

# make a mother wavelet

mother_sig = full_signal[int(mother_wavelet_bounds[0]* sampling_rate):int(mother_wavelet_bounds[1] * sampling_rate)]
times = np.array(list(range(len(mother_sig))))/sampling_rate + mother_wavelet_bounds[0]

#plt.plot(mother_sig, color='blue')


order_1 = 3
order_2 = 1
order_3 = 2
poly_1_lim = 23315
poly_2_lim = 23781

poly_1_x = np.arange(0, poly_1_lim, step=1)
poly_2_x = np.arange(poly_1_lim, poly_2_lim, step=1)
poly_3_x = np.arange(poly_2_lim, len(mother_sig), step=1)

poly_1 = np.polyfit(poly_1_x, mother_sig[:poly_1_lim],order_1)
poly_2 = np.polyfit(poly_2_x, mother_sig[poly_1_lim:poly_2_lim],order_2)
poly_3 = np.polyfit(poly_3_x, mother_sig[poly_2_lim:],order_3)

poly_1_vals = np.sum([c * (poly_1_x ** (order_1 - i)) for i,c in enumerate(poly_1)], axis=0)
poly_2_vals = np.sum([c * (poly_2_x ** (order_2 - i)) for i,c in enumerate(poly_2)], axis=0)
poly_3_vals = np.sum([c * (poly_3_x ** (order_3 - i)) for i,c in enumerate(poly_3)], axis=0)

mother_wavelet_x = np.concatenate([poly_1_x, poly_2_x])
mother_wavelet = np.concatenate([poly_1_vals, poly_2_vals])
mother_wavelet = mother_wavelet
plt.plot(mother_wavelet_x, mother_wavelet)
#plt.show()
#
np.save('/home/trevor/smi_data/mother_wavelet.npy', mother_wavelet)

full_bounds = [6,9]
full_sig = full_signal[int(full_bounds[0]* sampling_rate):int(full_bounds[1] * sampling_rate)]
sig_samples = np.arange(0, len(full_sig), 1)
full_times = np.array(list(range(len(full_sig))))/sampling_rate + full_bounds[0]

matched = np.convolve(full_sig , np.flip(mother_wavelet), mode='same')
matched_flip = np.convolve(full_sig, mother_wavelet, mode='same')
matched_smooth = np.convolve(np.convolve(matched, np.ones(2000)/2000, mode = 'same'), np.ones(2000)/2000, mode='same')
matched_flip_smooth = np.convolve(np.convolve(matched_flip, np.ones(2000)/2000, mode = 'same'), np.ones(2000)/2000, mode='same')

maxima = signal.argrelextrema(matched_smooth, np.greater)[0]
minima = signal.argrelextrema(matched_smooth, np.less)[0]

maxima_flip = signal.argrelextrema(matched_flip_smooth, np.greater)[0]
minima_flip = signal.argrelextrema(matched_flip_smooth, np.less)[0]


filt_sig = signal.medfilt(full_sig, 101)

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(sig_samples, matched_smooth, 'g-')
#ax1.set_ylim([875, 1000])
ax2.plot(sig_samples, filt_sig, 'b-', linewidth=0.6)


min_sig = np.min(filt_sig)
max_sig = np.max(filt_sig)

# for m in maxima:
#     ax2.plot([m, m], [min_sig, max_sig], linewidth=1, color='orange')
for m in maxima:
    ax2.plot([m + len(mother_wavelet), m + len(mother_wavelet)], [min_sig, max_sig], linewidth=1, color='red')

# for m in maxima_flip:
#     ax2.plot([m - len(mother_wavelet), m - len(mother_wavelet)], [min_sig, max_sig], linewidth=1, color='yellow')

fig.show()
plt.show()



print("")

