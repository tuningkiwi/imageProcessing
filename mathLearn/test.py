import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
#np.random.seed(19680801)

x = np.linspace(0.01,2,100)
y = np.exp(x)/(x**2)
#y = (4*(x**2)+3*(x))/2*x-7

print(y)
#z = np.sqrt(x**2 + y**2)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()


# #fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, layout="constrained")
# fig, axs = plt.subplots(1)

# axs.scatter(x,y,"bo")
# plt.show()

# # Matplotlib marker symbol
# axs[0, 0].scatter(x, y, s=80, c=z, marker=">")
# axs[0, 0].set_title("marker='>'")

# # marker from TeX: passing a TeX symbol name enclosed in $-signs
# axs[0, 1].scatter(x, y, s=80, c=z, marker=r"$\clubsuit$")
# axs[0, 1].set_title(r"marker=r'\$\clubsuit\$'")

# # marker from path: passing a custom path of N vertices as a (N, 2) array-like
# verts = [[-1, -1], [1, -1], [1, 1], [-1, -1]]
# axs[0, 2].scatter(x, y, s=80, c=z, marker=verts)
# axs[0, 2].set_title("marker=verts")

# # regular pentagon marker
# axs[1, 0].scatter(x, y, s=80, c=z, marker=(5, 0))
# axs[1, 0].set_title("marker=(5, 0)")

# # regular 5-pointed star marker
# axs[1, 1].scatter(x, y, s=80, c=z, marker=(5, 1))
# axs[1, 1].set_title("marker=(5, 1)")

# # regular 5-pointed asterisk marker
# axs[1, 2].scatter(x, y, s=80, c=z, marker=(5, 2))
# axs[1, 2].set_title("marker=(5, 2)")

# plt.show()