import numpy as np
from PIL import Image
import matplotlib.pyplot as plt 

#img = np.asarray(Image.open('./testimg.png'))
color_img  = Image.open('./img/fruits.jpg')
print(np.shape(color_img))
plt.imshow(color_img)
plt.show()
