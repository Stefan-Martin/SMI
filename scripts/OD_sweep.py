import os
import numpy as np
import matplotlib.pyplot as plt


base_dir = "/home/trevor/smi_data/OD_sweep/24-01-20_3/"
sampling_rate = 60e3
max_dac = 2 ** 12

od_data = {
    #0:"5mum_s_solid_OD0.npy",
    1: ("5mum_s_solid_OD1.npy", 6),
    0.1: ("5mum_s_solid_OD01.npy", 0),
    0.2: ("5mum_s_solid_OD02.npy", 1),
    0.3: ("5mum_s_solid_OD03.npy", 2),
    0.4: ("5mum_s_solid_OD04.npy", 3),
    0.5: ("5mum_s_solid_OD05.npy", 4),
    0.6: ("5mum_s_solid_OD06.npy", 5),
    # 0.7: ("5mum_s_solid_OD07.npy", 6),
    # 0.8: ("5mum_s_solid_OD08.npy", 7)
}

plot, axs = plt.subplots(nrows=7, ncols=2)

for OD, file in od_data.items():
    f = file[0]
    order = file[1]
    data = np.load(os.path.join(base_dir, f))
    axs[order][0].plot(np.array(list(range(len(data))))/sampling_rate, data/max_dac, linewidth=0.1)

    axs[order][0].set_ylabel("OD {}".format(OD))
    axs[order][0].set_xlim([9, 9.25])
    axs[order][1].set_xlim([13.5, 13.75])
    #axs[order][0].set_ylim([0.45, 0.6])
    #axs[order][1].set_ylim([0.45, 0.6])
    axs[order][1].plot(np.array(list(range(len(data)))) / sampling_rate,
                       data / max_dac, linewidth=0.1)


    if not order ==6:
        axs[order][0].set_xticks([])
        axs[order][1].set_xticks([])
    else:
        axs[order][1].set_xlabel("time (s)")
        axs[order][0].set_xlabel("time (s)")
#plot.tight_layout()
plot.show()
plot.set_size_inches((9 , 9))
print()
#plot.savefig(os.path.join(base_dir, 'od_sweep.svg'))
