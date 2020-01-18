import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import os

max_dac = 2 ** 12

output_dir = "/home/trevor/smi_data/OD_sweep"
os.makedirs(output_dir, exist_ok=True)

files = [
    "/home/trevor/smi_data/OD_sweep/5mum_s_solid_OD04.npy",
]

stationary_windows = [
    [(13 * 300e3,14.5 * 300e3)],
]
freqs = []
perdiograms = []
for i,(file, windows) in enumerate(zip(files, stationary_windows)):
    data = np.load(file)
    data =data/max_dac

    for window in windows:
        dual_plot, dual_ax = plt.subplots(nrows=2, ncols=1)
        slice_data = data[int(window[0]): int(window[1])]
        dual_ax[0].plot(np.array(list(range(len(slice_data))))/300000, slice_data)
        perd = signal.welch(slice_data.flatten() - np.mean(slice_data), fs=800000, nperseg=500000)
        perdiograms.append(perd[1])
        if i == 0:
            freqs = perd[0]
        dual_ax[1].plot(perd[0][1:], perd[1][1:])
        dual_ax[1].set_yscale('log')
        dual_ax[1].set_xscale('log')
        dual_ax[0].set_ylabel('Normalized Time Signal')
        dual_ax[0].set_xlabel('time (s)')
        dual_ax[1].set_ylabel(r'Power Spectral Density $\left( \frac{V^2}{Hz} \right)$')
        dual_ax[1].set_xlabel('Frequency (Hz)')
        dual_ax[1].set_xlim([0,100000])
        dual_plot.savefig(os.path.join(output_dir, 'forward_spectrum_OD04.svg'.format(i)))

avg_perdiogram = np.mean(perdiograms, axis=0)
plot, ax = plt.subplots(nrows=1, ncols=1)
ax.plot(freqs, avg_perdiogram)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_ylabel('Normalized Time Signal')
ax.set_title('Measured EC4 Noise PSD')
ax.set_xlabel('time (s)')
ax.set_ylabel(r'Power Spectral Density $\left( \frac{V^2}{Hz} \right)$')
ax.set_xlabel('Frequency (Hz)')
plot.savefig(os.path.join(output_dir, 'average_zoom.svg'))
print("")




