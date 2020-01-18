import matplotlib.pyplot as plt
import numpy as np

a=np.load('/home/trevor/smi_data/repeat/17-01-2020/5mum_s_solid_OD04_0.npy')
b=np.load('/home/trevor/smi_data/repeat/17-01-2020/5mum_s_solid_OD04_60.npy')
c=np.load('/home/trevor/smi_data/repeat/17-01-2020/5mum_s_solid_OD04_120.npy')
d=np.load('/home/trevor/smi_data/repeat/17-01-2020/5mum_s_solid_OD04_180.npy')
plt.plot(np.array(list(range(len(a))))/300e3, a/(2**12), linewidth=0.1, label='0 mins')
#plt.plot(np.array(list(range(len(b))))/300e3, b/(2**12), linewidth=0.1, label='20 mins')
#plt.plot(np.array(list(range(len(c))))/300e3, c/(2**12), linewidth=0.1, label='40 mins')
#plt.plot(np.array(list(range(len(c))))/300e3, d/(2**12), linewidth=0.1, label='60 mins')
plt.xlim([12.5, 13])
plt.ylabel('normalized DAQ tics')
plt.xlabel('time (s)')
plt.legend()
#plt.xlim([13.5, 14])
plt.tight_layout()
fig = plt.gcf()
fig.set_size_inches(9, 3)
#plt.savefig("/home/trevor/smi_data/repeat/1_hr_drift.svg")
#plt.savefig("/home/trevor/smi_data/repeat/1_hr_drift.png")

plt.show()
print("")

