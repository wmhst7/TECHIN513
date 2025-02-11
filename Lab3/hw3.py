import numpy as np
import matplotlib.pyplot as plt

def X(k):
    if k == 0:
        return 2/3
    else:
        return (1/6) * np.exp(-1j * np.pi/2 * k) * (np.sin(2 * np.pi * k / 3) / np.sin(np.pi * k / 6))

k_values = np.arange(6)
X_values = np.array([X(k) for k in k_values])

magnitude = np.abs(X_values)
phase = np.angle(X_values)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.stem(k_values, magnitude, basefmt=" ")
plt.title('Magnitude Spectrum')
plt.xlabel('k')
plt.ylabel('|X[k]|')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.stem(k_values, phase, basefmt=" ")
plt.title('Phase Spectrum')
plt.xlabel('k')
plt.ylabel('∠X[k] (radians)')
plt.grid(True)

plt.tight_layout()
plt.show()