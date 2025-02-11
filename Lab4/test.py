import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
f1 = 5  # Hz
f2 = 20  # Hz
fs_list = [50, 25, 15]  # Sampling rates
t_start = 0
t_end = 1  # seconds

# High-resolution original signal
t_high = np.linspace(t_start, t_end, 1000)
x_high = np.sin(2 * np.pi * f1 * t_high) + np.sin(2 * np.pi * f2 * t_high)

# Create plots
plt.figure(figsize=(10, 8))

for i, fs in enumerate(fs_list, 1):
    plt.subplot(3, 1, i)
    plt.plot(t_high, x_high, 'b-', label='Original Signal')
    
    # Generate sampled signal
    t_sampled = np.arange(t_start, t_end + 1/fs, 1/fs)  # Include t_end if divisible
    t_sampled = t_sampled[t_sampled <= t_end]  # Ensure not exceeding t_end
    x_sampled = np.sin(2 * np.pi * f1 * t_sampled) + np.sin(2 * np.pi * f2 * t_sampled)
    
    # Plot sampled points
    # plt.stem(t_sampled, x_sampled, linefmt='r-', markerfmt='ro', basefmt=' ', label='Samples')
    plt.plot(t_sampled, x_sampled, 'r.', label='Samples')
    
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title(f'Sampling Rate: {fs} Hz')
    plt.legend(loc='upper right')
    plt.grid(True)

plt.tight_layout()
plt.show()