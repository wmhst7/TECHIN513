import numpy as np
import matplotlib.pyplot as plt

# Define the original signal
def original_signal(n):
    if n in [0, 1, 2, 3]:
        return 1
    else:
        return 0

# Define the DTFS coefficients
def X(k):
    if k == 0:
        return 2/3
    else:
        return (1/6) * np.exp(-1j * np.pi/2 * k) * (np.sin(2 * np.pi * k / 3) / np.sin(np.pi * k / 6))

# Reconstruct the signal using inverse DTFS
def reconstruct_signal(n, N):
    signal = 0
    for k in range(N):
        signal += X(k) * np.exp(1j * 2 * np.pi * k * n / N)
    return signal.real


N = 6
n_values = np.arange(N)
original_values = np.array([original_signal(n) for n in n_values])
reconstructed_values = np.array([reconstruct_signal(n, N) for n in n_values])

# Plotting
plt.figure(figsize=(10, 6))

# Original signal
plt.subplot(2, 1, 1)
plt.stem(n_values, original_values, basefmt=" ", label='Original Signal')
plt.title('Original Signal')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.legend()

# Reconstructed signal
plt.subplot(2, 1, 2)
plt.stem(n_values, reconstructed_values, basefmt=" ", label='Reconstructed Signal', markerfmt='ro')
plt.title('Reconstructed Signal')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()