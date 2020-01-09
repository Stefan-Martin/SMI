f_samp = 10000;
amplitude_wavelengths = 100;
SNR=10;
Noisy=1;
[out,in] = smi_signal_simulation(f_samp,1,f_samp,amplitude_wavelengths,0,6,3);
if Noisy
    out = awgn(out,SNR)
end
ax1 = subplot(2,1,1);
plot(ax1,out)
title(ax1, "Input and Resulting SMI Signal")
ylabel(ax1, "Smi Signal (V)")

ax2 = subplot(2,1,2);
plot(ax2,in)
ylabel(ax2, "Input Displacement (x/\lambda)")
xlabel(ax2, "Time (samples)")
