import enum
import numpy as np
import matplotlib.pyplot as plt

π = np.pi
a = 1000 * np.pi
w0 = 2 * π / 0.005 
N = int(30000 / w0)
n = np.arange(-N, N + 1, 1)
wn = np.arange(-N, N + 1, 1)* w0
Xn = np.zeros_like(wn, dtype=complex)
Hn = np.zeros_like(wn, dtype=complex)

for i in range(len(n)):
    Hn[i] = (a**2) / (a + 1j * wn[i])**2
    if n[i] == 0:
        Xn[i] = 0
    else:
        Xn[i] = 2 * np.pi * 1j * (-1)**np.abs(n[i]) / (np.pi * n[i])

Yn = Xn * Hn
Ns = [np.arange(-1, 2), np.arange(-2, 3), np.arange(-10, 11), np.arange(-20, 21)]
t = np.arange(0, 0.015, 0.0001)
y = np.zeros((4, len(t)), dtype=complex)

for i, N_range in enumerate(Ns):
    sum = 0
    for n in N_range:
        index = N + n 
        sum += Yn[index] * np.exp(1j * n * w0 * t)
    sum = (sum * (1/(2*π)))
    y[i] = sum

plt.plot(t, y[0], label="N=1")
plt.plot(t, y[1], label="N=2")
plt.plot(t, y[2], label="N=10")
plt.plot(t, y[3], label="N=20")
plt.xlabel("t / ms")
plt.ylabel("y(t)")
plt.grid()
plt.legend()
plt.show()

