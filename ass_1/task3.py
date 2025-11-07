import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd

a = 1000 * np.pi
dt = 0.00001
t2 = np.arange(0, 0.02, dt)
imp_response = (a ** 2) * t2 *np.exp(-a * t2)

x1 = np.sin(2 * np.pi * 100 * t2)
x2 = np.sin(2 * np.pi * 1000 * t2)

dirac = np.zeros(t2.shape)
dirac[0] = 1/dt

y1 = dt * signal.convolve(imp_response, x1, method="direct")
y1 = y1[0 : dirac.shape[0]]

y2 = dt * signal.convolve(imp_response, x2, method="direct")
y2 = y2[0 : dirac.shape[0]]

y3 = dt * signal.convolve(imp_response, x1 + x2, method="direct")
y3 = y3[0 : dirac.shape[0]]
 
fig, ax = plt.subplots()
        
ax.plot(t2 * 1000, y1, label="y1")
ax.plot(t2 * 1000, y2, label="y2")
ax.plot(t2 * 1000, y3, label="y3")
# ax.plot(t2 * 1000, x1, label="x1")
# ax.plot(t2 * 1000, x2, label="x2")
plt.xlabel("tid")
plt.ylabel("amplitud")
plt.grid()
plt.legend()
plt.show()
