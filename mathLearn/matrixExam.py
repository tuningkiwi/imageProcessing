import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.array([[1,2],[3,4]])
si = np.linalg.inv(t)
sii = t.dot(si)

fig, ax = plt.subplots()
ax.scatter(t, sii, s=80, marker=">")

ax.set(xlabel='x', ylabel='y',
       title='matrix')
ax.grid()

fig.savefig("test.png")
plt.show()