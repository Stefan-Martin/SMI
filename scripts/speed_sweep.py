import os
import numpy as np
import matplotlib.pyplot as plt

base_dir = "/home/trevor/smi_data/speed/17-01-2020/"
sampling_rate = 300e3
max_dac = 2 ** 12

od_data = {

    10: ("10mum_s_solid_OD04.npy", 4),
    7: ("7mum_s_solid_OD04.npy", 3),
    5: ("5mum_s_solid_OD04.npy", 2),
    2.5: ("2.5mum_s_solid_OD04.npy", 1),
    1: ("1mum_s_solid_OD04.npy", 0)
}


plot, axs = plt.subplots(nrows=5, ncols=1)

for speed, file in od_data.items():
    f = file[0]
    order = file[1]
    data = np.load(os.path.join(base_dir, f))
    axs[order].plot(np.array(list(range(len(data))))/sampling_rate, data/max_dac, linewidth=0.1)
    axs[order].set_xlim([9.9,10.4])
    axs[order].set_ylabel(r"{} $\mu m/s$ ".format(speed))

    if order ==4:
        axs[order].set_xlabel("time (s)")
    else:
        axs[order].set_xticks([])

plot.show()
plot.set_size_inches((9 , 9))
