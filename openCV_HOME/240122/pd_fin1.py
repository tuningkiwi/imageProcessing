import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import cm 

#set up a figure twice as tall as it is wide
fig = plt.figure (figsize=plt.figaspect(2.))
#fig = plt.figure ()

fig.suptitle('a tale of 2 subplots')

#first subplot
ax = fig.add_subplot(2,1,1,projection='3d')

w0 = np.arange(-2,2,0.25)
w1 = np.arange(-2,2,0.25)
w0, w1 = np.meshgrid(w0,w1)
z = w0**2 +2*w0*w1+3

ax.plot_surface(w0,w1,z,vmin = z.min()*2, cmap=cm.Blues)
ax.set(xlabel='w0',ylabel='w1',zlabel='z')

#second subplot 
ax = fig.add_subplot(2,1,2)

w0 = np.arange(-2,2,0.25)
w1 = -1
z = w0**2 +2*w1*w0+3

ax.plot(w0,z,'b-')

plt.show()
