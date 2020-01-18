import os
import numpy as np
import glob
import re
import matplotlib.pyplot as plt

base_dir = "/home/trevor/smi_data/repeat/17-01-2020/"

pivot = "5mum_s_solid_OD04_0.npy"
pivot_data = np.load(os.path.join(base_dir, pivot))/(2**12)
range = [int(len(pivot_data)/3),2 * int(len(pivot_data)/3)]
pivot_data = pivot_data[range[0]:range[1]]
pivot_data = pivot_data - np.mean(pivot_data)

iterations = []
avg_signal = np.copy(pivot_data)
distances = []
for file in glob.glob(os.path.join(base_dir, '*.npy')):
    iteration_no = int(re.search('OD04_(.*).npy', file).group(1))
    iterations.append(iteration_no)
    this_sig = np.load(file)/(2**12)
    this_sig = this_sig[range[0]:range[1]]
    this_sig = this_sig - np.mean(this_sig)
    avg_signal += this_sig
    distance = np.sum(np.abs(pivot_data - this_sig + np.mean(this_sig)))
    distances.append(distance)

avg_signal = avg_signal/len(iterations)


distance_plt, distance_ax = plt.subplots(nrows=1, ncols=1)

s = sorted(zip(distances, iterations), key=lambda x:x[1])
distance_ax.plot([x[1] for x in s], np.array([x[0] for x in s])/len(pivot_data))
distance_ax.set_xlabel('Iteration')
distance_ax.set_ylabel('Mean difference (V)')
distance_plt.show()
print("")
