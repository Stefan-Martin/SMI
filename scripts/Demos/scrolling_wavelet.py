import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from realtime_plot import RealtimePlotter

meta=np.load('/home/stefan/smi_data/14-02-2020/0.01mm_2_meta.npy')
full_signal=np.load('/home/stefan/smi_data/14-02-2020/0.01mm_2.npy').flatten()/(2 ** 12)
sampling_rate = int(meta[5]) #read in sampling rate info from metadata
process_time_bounds = [0.5, 5]
reduced_signal = full_signal[int(process_time_bounds[0]* sampling_rate):int(process_time_bounds[1] * sampling_rate)]

b, a = signal.butter(4,550,btype='low',fs=sampling_rate) #lowpass filter
filtered = signal.lfilter(b, a, reduced_signal)
plt.plot(filtered)
plt.show()

class _SinePlotter(RealtimePlotter):

    def __init__(self):
        RealtimePlotter.__init__(self, [(+.35, +.65), (-1, +1)],
                                 show_yvals=True,
                                 window_name='Signal',
                                 yticks=[(+.35, +.5, +.65), (-1, 0, +1)],
                                 styles=['r', 'b-'],
                                 ylabels=['Signal', 'Wavelet Transform'])

        self.xcurr = 0

    def getValues(self):
        return filtered[self.xcurr],0

    def _getWave(self, k):
        size = len(self.x)

        return np.sin(2 * k * np.pi * (float(self.xcurr) % size) / size)


def _update(plotter):
    from time import sleep

    while True:
        plotter.xcurr += 5
        sleep(.0005)


if __name__ == '__main__':
    import threading

    plotter = _SinePlotter()

    thread = threading.Thread(target=_update, args=(plotter,))
    thread.daemon = True
    thread.start()

    plotter.start()
