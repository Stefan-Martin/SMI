import numpy as np

from scipy import signal, integrate
import multiprocessing
import os

sampling_rate = 300000
analysis_bounds = [7, 10]

full_signal=np.load('target_on.npy').flatten()/(2 ** 12)

# make a mother wavelet

mother_sig = full_signal[int(analysis_bounds[0]* sampling_rate):int(analysis_bounds[1] * sampling_rate)]
sample_nums =  np.arange(0, len(mother_sig), 1)
times =sample_nums/sampling_rate + analysis_bounds[0]

def morlet_wavelet(t, omega_0):
    return np.exp(1j * omega_0 * t) * np.exp(-1 * t**2 / 2)

def wavelet_transform_fcn(a,b, sig, t):
    t_i=int(t)
    return 1/np.sqrt(a) * sig[t_i] * morlet_wavelet((t-b)/a, 5.336)

def wavelet_transform_integral(inp):
    a = inp[0]
    b = inp[1]
    sig = inp[2]
    total = inp[3]
    n = inp[4]
    print('{}/{}'.format(n, total))
    int_func = lambda t: wavelet_transform_fcn(a,b, sig, t)
    return integrate.quad(int_func, 0, len(sig))[0]



delta_b = 500
b_0 = 0
b_max = len(mother_sig)
b_vals = np.arange(b_0, b_max, step=delta_b)
a_0 = 1000
a_max = 40000
a_steps = 25
a_vals = np.arange(a_0, a_max, step=(a_max - a_0)/a_steps)
#wavelet_vals = [morlet_wavelet(i/10000, 5.336) for i in sample_nums]



dispatch = []
total = len(a_vals) * len(b_vals)
for i,a_val in enumerate(a_vals):
    for j,b_val in enumerate(b_vals):
        dispatch.append((a_val, b_val, mother_sig, total, (i+1) * (j+1)))

with multiprocessing.Pool() as p:
    res = p.map(wavelet_transform_integral, dispatch)


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

res = list(res)
res = list(divide_chunks(res, len(b_vals)))


dir = '/wavelets/'
os.makedirs(dir, exist_ok=True)
np.save(os.path.join(dir,'morlet_wvlet_results.npy'), res)
np.save(os.path.join(dir,'morlet_wvlet_a_vals.npy'), a_vals)
np.save(os.path.join(dir,'morlet_wvlet_b_vals.npy'), b_vals)
np.save(os.path.join(dir,'morlet_sig.npy'), mother_sig)
np.save(os.path.join(dir,'morlet_bins.npy'), sample_nums)
np.save(os.path.join(dir,'morlet_times.npy'), times)


print("")













