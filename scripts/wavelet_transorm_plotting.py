import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import cv2

results = np.load('/home/trevor/smi_data/wavelets/tight_long/morlet_wvlet_results.npy')
a_vals = np.load('/home/trevor/smi_data/wavelets/tight_long/morlet_wvlet_a_vals.npy')
b_vals = np.load('/home/trevor/smi_data/wavelets/tight_long/morlet_wvlet_b_vals.npy')
mother_sig = np.load('/home/trevor/smi_data/wavelets/tight_long/morlet_sig.npy')
sample_nums = np.load('/home/trevor/smi_data/wavelets/tight_long/morlet_bins.npy')
sample_times = np.load('/home/trevor/smi_data/wavelets/tight_long/morlet_times.npy')

results_re = cv2.resize(results, (len(b_vals), len(b_vals)))

plt.imshow(results,  interpolation='none', extent=[np.min(b_vals),np.max(b_vals), np.min(a_vals),np.max(a_vals)], aspect=1/7 * len(b_vals)/len(a_vals))
plt.xlabel(r'$b \propto t$')
plt.ylabel(r'$a \propto \frac{1}{f}$')
plt.show()
plt.figure()

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(sample_nums, signal.medfilt(mother_sig, 101), 'g-', linewidth = 0.2)

plt.show()

print("")



