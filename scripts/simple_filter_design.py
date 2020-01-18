from scipy import signal
import numpy as np

import matplotlib.pyplot as plt


sampling_freq = 300000

cutoff_hz = 300000/3

cutoff_N = cutoff_hz/(sampling_freq/2)

#num_coeff, denom_coeff = signal.cheby1(5,)

sig = np.load("/home/trevor/smi_data/OD_sweep/neg_1.npy")/(2**12)

#out = signal.lfilter(num_coeff, denom_coeff, sig)

MA_size = 100
f = np.ones((MA_size,1))/MA_size
out = signal.convolve(sig, f)

dual_plot, dual_ax = plt.subplots(nrows=2, ncols=1)


xlim = [13, 13.4]
dual_ax[0].plot(np.array(list(range(len(sig))))/sampling_freq, sig, linewidth = 0.1)
dual_ax[0].set_xlim(xlim)
dual_ax[1].plot(np.array(list(range(len(out))))/sampling_freq, out, linewidth = 1)
dual_ax[1].set_xlim(xlim)
dual_plot.show()




# w, h =  signal.freqz(num_coeff, denom_coeff)
#
# filt_fig, filt_ax = plt.subplots()
# filt_ax.set_title('Digital filter frequency response')
# filt_ax.plot(w, 20 * np.log10(abs(h)), 'b')
# filt_ax.set_ylabel('Amplitude [dB]', color='b')
# filt_ax.set_xlabel('Frequency [rad/sample]')
# filt_ax.set_yscale('log')
# filt_ax.set_xscale('log')
# ax2 = filt_ax.twinx()
# angles = np.unwrap(np.angle(h))
# ax2.plot(w, angles, 'g')
# ax2.set_ylabel('Angle (radians)', color='g')
# ax2.grid()
# ax2.axis('tight')
# filt_fig.show()


print("")
