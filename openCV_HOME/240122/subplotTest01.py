import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,5,0.1)
y1 = np.cos(x)
y2 = np.exp(x)
y3 = 2**x

plt.subplot(311)
plt.plot(x,y1)
plt.title("y=cos(x)")

plt.subplot(312)
plt.plot(x,y2)
plt.title("y= exp(x)")

plt.subplot(313)
plt.plot(x,y3)
plt.title("y = 2**x")
plt.show()