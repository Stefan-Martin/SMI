import simpleaudio as sa
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io.wavfile import write
upper_bound=10
process_time_bounds = [0, upper_bound]
audio_frequency=192000

meta=np.load('/home/stefan/smi_data/14-02-2020/0.01mm_2_meta.npy')
full_signal=np.load('/home/stefan/smi_data/14-02-2020/0.01mm_2.npy').flatten()/(2 ** 12)
sampling_rate = 400000#int(meta[5]) #read in sampling rate info from metadata

reduced_signal = full_signal[int(process_time_bounds[0]* sampling_rate):int(process_time_bounds[1] * sampling_rate)]
times = np.array(list(range(len(reduced_signal))))/sampling_rate + process_time_bounds[0]


audio=signal.resample(reduced_signal,upper_bound*audio_frequency)
audio=audio*(2**15 - 1) / np.max(np.abs(audio))
audio=audio.astype(np.int16)
plt.plot(audio)

play_obj = sa.play_buffer(audio, 1, 2, audio_frequency)
plt.show()
play_obj.wait_done()
write('/home/stefan/smi_data/14-02-2020/Fringes.wav', audio_frequency, audio)  # Save as WAV file
print("")