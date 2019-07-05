import os
import numpy as np
from scipy.signal import find_peaks_cwt
from scipy.ndimage import convolve

import matplotlib.pyplot as plt

if __name__=="__main__":
    data_path = os.path.join(os.getenv('HOME'),'interferometry_data/40_micron_1.csv')
    plt.figure(figsize=(12,4))

    data = np.genfromtxt(data_path,delimiter=',')
    data=data[1:,0:2]
    voltage=data[:,1]
    domain_0 = [1000,6000]
    domain_1 = [6000,15000]
    domain_2= [15000,24000]
    voltage=(voltage-np.mean(voltage)) # normalize
    #voltage = convolve(voltage,np.ones(30)/30)
    #voltage = convolve(voltage, np.ones(20) / 20)
    peaks=[]
    peaks += list(find_peaks_cwt(voltage[domain_0[0]:domain_0[1]],np.arange(50,200)) + domain_0[0])
    peaks += list(find_peaks_cwt(voltage[domain_1[0]:domain_1[1]],np.arange(1,100)) + domain_1[0])
    peaks += list(find_peaks_cwt(voltage[domain_2[0]:domain_2[1]], np.arange(100, 300)) +domain_2[0])
    plt.xlabel('time (counts)')
    plt.ylabel('Voltage (V)')
    plt.title('{} Peaks, predicted length {} microns'.format(len(peaks), 0.65 * len(peaks)))
    #[plt.axvline(peak , color = 'red', linewidth = 0.2) for peak in peaks]
    plt.plot(list(range(len(voltage))), voltage, linewidth = 0.3, color = 'blue')
    plt.savefig(os.path.join(os.path.dirname(data_path),'peaks.png'),dpi = 1500)
    print("")