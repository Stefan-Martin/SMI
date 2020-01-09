import os
import numbers
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

input_displacement_path = os.path.join(os.getenv('HOME'),'interferometry_data/15SNR_in.csv')
smi_signal_path = os.path.join(os.getenv('HOME'),'interferometry_data/15SNR_out.csv')

input_diplacement = np.genfromtxt(input_displacement_path, delimiter=',')[:10000]
smi_signal = np.genfromtxt(smi_signal_path, delimiter=',')[:10000]

matplotlib.rcParams['figure.dpi'] = 300
fig, (ax1, ax2,) = plt.subplots(2, figsize=(8, 8))
ax1.plot(input_diplacement, linewidth=1)
ax1.set_ylabel('Input Displacement (x/λ)')
ax2.plot(smi_signal, linewidth = 1)
ax2.set_ylabel('SMI Signal (V)')
fig.suptitle('Signal Plot SNR15 (C=3, α=6)')
limits = [0,10000]
ax1.set_xlim(limits)
ax2.set_xlim(limits)
plt.savefig(os.path.join(os.getenv('HOME'),'interferometry_data/15SNRplot.png'))