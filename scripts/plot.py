import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from medpy.filter.smoothing import anisotropic_diffusion
import cv2

a=np.load('/home/trevor/smi_data/OD_sweep/24-01-20_3/5mum_s_solid_OD03_3.npy')
b=np.load('/home/trevor/smi_data/OD_sweep/24-01-20_3/5mum_s_solid_OD03_4.npy')
c=np.load('/home/trevor/smi_data/OD_sweep/24-01-20_3/5mum_s_solid_OD03_5.npy')
d=np.load('/home/trevor/smi_data/OD_sweep/24-01-20_3/5mum_s_solid_OD03_6.npy')
e=np.load('/home/trevor/smi_data/OD_sweep/24-01-20_3/5mum_s_solid_OD03_7.npy')
f=np.load('/home/trevor/smi_data/OD_sweep/24-01-20_3/5mum_s_solid_OD03_8.npy')
g=np.load('/home/trevor/smi_data/OD_sweep/24-01-20_3/5mum_s_solid_OD03_9.npy')
h=np.load('/home/trevor/smi_data/OD_sweep/24-01-20_3/5mum_s_solid_OD03_10.npy')
i=np.load('/home/trevor/smi_data/OD_sweep/24-01-20_3/5mum_s_solid_OD03_11.npy')
j=np.load('/home/trevor/smi_data/OD_sweep/24-01-20_3/5mum_s_solid_OD03_12.npy')
k=np.load('/home/trevor/smi_data/OD_sweep/24-01-20_3/5mum_s_solid_OD03_13.npy')
l=np.load('/home/trevor/smi_data/OD_sweep/24-01-20_3/5mum_s_solid_OD03_14.npy')
m=np.load('/home/trevor/smi_data/OD_sweep/24-01-20_3/5mum_s_solid_OD03_15.npy')
n=np.load('/home/trevor/smi_data/OD_sweep/24-01-20_3/5mum_s_solid_OD03_16.npy')
# b = np.load('/home/trevor/smi_data/misc/jank_lens_left.npy')
# c = np.load('/home/trevor/smi_data/misc/jank_lens_right.npy')

#reduced_signal = a[int(5* 300000):int(8 * 300000)].flatten()

#filt_1 = reduced_signal
#filt_2 = signal.medfilt(signal.medfilt(reduced_signal, 81), 81)
#filt_3 = cv2.bilateralFilter(np.array(reduced_signal, dtype=np.float32),51, 150, 150)



#b=np.load('/home/trevor/smi_data/stage_emi_test/manual_stage.npy')
#b=np.load('/home/trevor/smi_data/stage_emi_test/target_off.npy')
#c=np.load('/home/trevor/smi_data/stage_emi_test/stationary_target.npy')

plot, axs = plt.subplots(nrows=1, ncols=1)

#axs.plot(g, label = '35.6', linewidth = 0.2)
axs.plot(n, label = '34.5', linewidth = 0.2)
axs.plot(j, label = '35.0', linewidth = 0.2)
axs.plot(m, label = '35.6', linewidth = 0.2)
#axs.plot(k, label = '36.4', linewidth = 0.2)
#axs.plot(l, label = '36.8', linewidth = 0.2)


# axs.plot(b, label = 'left')
# axs.plot(c, label = 'right')
axs.legend()
plot.show()

print("")


# axs[0].plot(np.array(list(range(len(filt_1))))/300e3, filt_1/(2**12), linewidth=0.5, label = 'unfiltered', color='blue')
# #axs[0].plot(np.array(list(range(len(filt_2))))/300e3, filt_2/(2**12), linewidth=0.5, label='second', color='red')
# axs[0].plot(np.array(list(range(len(filt_3))))/300e3, filt_3/(2**12), linewidth=0.5, label='bilateral filter', color='red')
#
# grad = np.gradient(filt_1, axis=0)
# #grad_diffusion = np.gradient(filt_2, axis=0)
# grad_3 = np.gradient(filt_3, axis=0)
# mean_grad = np.mean(grad_3/(2**12))
# std_grad = np.std(grad_3/(2**12))
# axs[1].plot(np.array(list(range(len(grad))))/300e3, grad/(2**12), label = 'unfiltered', linewidth=0.5, color='blue')
# #axs[1].plot(np.array(list(range(len(grad_diffusion))))/300e3, grad_diffusion/(2**12), linewidth=0.5, color='red')
# axs[1].plot(np.array(list(range(len(grad_3))))/300e3, grad_3/(2**12),  label = 'bilateral filter',linewidth=0.5, color='red')
# axs[1].plot([0,10], [mean_grad + 3 * std_grad,mean_grad + 3 * std_grad], label = r'$\pm 3 \sigma$', linewidth=1, color='g')
# axs[1].plot([0,10], [mean_grad - 3 * std_grad,mean_grad - 3 * std_grad], linewidth=1, color='g')
#
# axs[1].legend(loc='lower left')
# #axs[1].plot(np.array(list(range(len(a))))/300e3, b/(2**12), linewidth=0.1)
#
# axs[0].set_ylabel('Voltagae (V)')
# axs[1].set_ylabel(r'$ \frac{dV}{dt}$(V/s)')
# #axs[1].set_ylabel('manual stage signal')
# axs[1].set_xlabel('time (s)')
# axs[0].set_xlim([1.4, 1.44])
# axs[1].set_xlim([1.4, 1.44])
#
# #axs[0].set_xlim([0.33, 0.34])
# #axs[1].set_xlim([0.33, 0.34])
#
# #axs[0].set_xlim([0.345, 0.3525])
# #axs[1].set_xlim([0.345, 0.3525])
#
# plot.set_size_inches(9, 6)
# #plt.savefig("/home/trevor/smi_data/stage_emi_test/configs.svg")
# #plt.savefig("/home/trevor/smi_data/stage_emi_test/configs.png")

plot.show()
print("")

