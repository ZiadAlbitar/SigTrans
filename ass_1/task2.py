import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd

a = 1000 * np.pi
t2 = np.arange(0, 0.005, 0.00001)
dt = t2[1] - t2[0]

imp_response = (a ** 2) * t2 *np.exp(-a * t2)

dirac = np.zeros(t2.shape)
dirac[0] = 1/dt


convolution = dt * signal.convolve(dirac, imp_response, method="direct")
convolution = convolution[0 : dirac.shape[0]]

fig, ax = plt.subplots()

ax.plot(t2 * 1000, imp_response, label="impulse_response")
ax.plot(t2 * 1000, convolution, label="convolution")
plt.xlabel("tid")
plt.ylabel("amplitud")
plt.grid()
plt.legend()
plt.show()
