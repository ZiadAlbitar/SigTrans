import numpy as np
import matplotlib.pyplot as plt

a = 1000 * np.pi
w = np.arange(-15e3, 15e3, 1)
H = (a**2) / (a + 1j * w)**2


fig, ax = plt.subplots(2, 1)
ax[0].plot(w, np.abs(H))
ax[1].plot(w, np.angle(H))
ax[0].grid()
ax[1].grid()
ax[0].set_xlabel("$\omega$ /rad/ s")
ax[1].set_xlabel("$\omega$ /rad/ s")
plt.show()



