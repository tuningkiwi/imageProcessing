import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import cm 

plt.style.use('_mpl-gallery')

#make data 
w0 = np.arange(-2,2,0.25)
w1 = np.arange(-2,2,0.25)
w0, w1 = np.meshgrid(w0,w1)
z = w0**2 +2*w0*w1+3

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
ax.plot_surface(w0,w1,z,vmin = z.min()*2, cmap=cm.Blues)
fig.suptitle('figure 1')
#ax.set_title('partial differentiation')
ax.set(xlabel='w0',ylabel='w1',zlabel='z')

plt.show()
