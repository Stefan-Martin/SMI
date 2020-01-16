import matplotlib.pyplot as plt
import numpy as np

a=np.load('5mum_s_solid_OD06.npy')
plt.plot(a,linewidth = 1)
#plt.xlim([4e6, 4e6 + 10000])
#plt.ylim([1300, 1600])
plt.show()
print("")

