import numpy as np

movement_speed_m_s = 1/1000
wavelength_m = (650*(10**-9))
desired_resoloution_m = 50 * (10**-9)
wavelengths_s = movement_speed_m_s / wavelength_m
minimum_samples_s = wavelengths_s*(wavelength_m/desired_resoloution_m) * 2
print("minimum sampling rate in Hz: {}".format(minimum_samples_s))
