import numpy as np
import matplotlib.pyplot as plt

π = np.pi
w0 = 2 * π / 0.005 
N = int(15000 / w0)
n = np.arange(-N, N + 1, 1)
wn = np.arange(-N, N + 1, 1)* w0
Xn = np.zeros_like(wn, dtype=complex)

for i in range(len(n)):
    if n[i] == 0:
        Xn[i] = 0
    else:
        Xn[i] = 2 * np.pi * 1j * (-1)**np.abs(n[i]) / (np.pi * n[i])

fig, ax = plt.subplots(2, 1)
ax[0].stem(wn, np.abs(Xn))
ax[1].stem(wn, np.angle(Xn))
ax[0].grid()
ax[1].grid()
ax[0].set_xlabel("$\omega$ /rad/ s")
ax[1].set_xlabel("$\omega$ /rad/ s")
plt.show()
