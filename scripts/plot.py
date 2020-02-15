import matplotlib.pyplot as plt
import numpy as np

a=np.load('/home/stefan/smi_data/14-02-2020/2mm_1.npy')
b=np.load('/home/stefan/smi_data/14-02-2020/2mm_1_meta.npy')

plot, axs = plt.subplots(nrows=1, ncols=1)

axs.plot(a, label = "OD="+str(b[2]), linewidth = 0.5)


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

