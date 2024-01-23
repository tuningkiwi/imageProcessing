#from PIL import Image

import matplotlib.pyplot as plt 
import numpy as np

#img = np.asarray(Image.open('./testimg.png'))

img = np.array([[[0,0,0],[255,0,0]],[[0,255,0],[0,0,255]]])

print(img)
# print(repr(img))
print(np.shape(img))
print(type(img))
subImg1 = img.copy()
#subImg1[:,:,]
# subImg1 +=3
# np.where(subImg1>255,255,subImg1)
#subImg1[:,:,2]=255


print(subImg1)
plt.imshow(subImg1)
plt.show()
#imgplot = plt.imshow(img)


