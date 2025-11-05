import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd

t0 = 0
t1 = 5
increment = 0.00001
tt = np.arange(t0, t1, increment)

x1 = np.sin(2 * np.pi * 100 * tt)
x2 = np.sin(2 * np.pi * 1000 * tt)

fig, ax = plt.subplots()

ax.plot(tt, x1, label="x_1")
ax.plot(tt, x2, label="x_2")
ax.set_xlim(0, 0.010)

plt.grid()
plt.legend()
plt.show()
sd.play(x1, 1/increment, blocking=True)
sd.play(x2, 1/increment, blocking=True)
