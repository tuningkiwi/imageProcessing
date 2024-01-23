import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import colormaps

#plt.style.use('_mpl-gallery-nogrid')
#plt.rcParams['axes.unicode_minus'] = False 

x = np.linspace(-2,2,100)
y = np.linspace(-1.3,1.3,100)

x,y = np.meshgrid(x,y)
z = x*np.exp(-x**2-y**2)
#figsize=(12,8)
fig = plt.figure(figsize=plt.figaspect(.5))
fig.set_facecolor('green')
ax = fig.add_subplot()
#myLevel = np.linspace(np.min(z), np.max(z),7)
con1 = ax.contour(x,y,z,levels=20, colors='c', linewidths =1, linestyles='-' )
con2 = ax.contour(x,y,z, levels = 256, cmap='jet')

ax.clabel(con1, con1.levels, inline=True)
fig.colorbar(con2, shrink=0.5)

plt.show()