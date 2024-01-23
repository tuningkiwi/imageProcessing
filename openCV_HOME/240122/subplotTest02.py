import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,5,0.1)
y1 = np.cos(x)
y2 = np.exp(x)
y3 = 2**x

fig, axs = plt.subplots(3,1)

axs[0].plot(x,y1)
axs[1].plot(x,y2)
axs[2].plot(x,y3)

plt.show()
