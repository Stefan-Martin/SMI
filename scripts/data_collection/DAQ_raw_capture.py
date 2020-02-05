

from __future__ import print_function

import time
from scripts.DAQ import comedi_async
import numpy as np
import os
import matplotlib.pyplot as plt
CONTROLLERNAME = 'E-873'  # 'C-884' will also work
STAGES = None
REFMODES = 'FRF'

def main():

    print('starting recording')

    res = comedi_async.sample_time_async([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 1000, 10)

    time.sleep(5)

    output = '/home/interferometry_data/'
    os.makedirs(output, exist_ok=True)
    data=res.get()
    for i in range(0, 3):

        plt.plot(np.array(list(range(len(data[:, i])))) / 1e3, data[:, i]*1.5*0.85/ (2 ** 12)-0.75, linewidth=0.5, label=str(i))

    plt.legend()
    plt.show()
    print('recording done')
    print("")

if __name__ == '__main__':
    main()