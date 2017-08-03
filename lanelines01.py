#extract lines by color selection

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# read the image
image = mpimg.imread('testlanelines.jpg')
print('This image is ', type(image), ' with dimensions', image.shape)

# Grab the x and y size and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]

# make a copy always!!
color_select = np.copy(image)

#set a threshold
red_th = 200
blue_th= 200
green_th = 200
rgb_threshold = [red_th, green_th, blue_th]

#identify pixels below the threshold
pixels = (image[:,:,0] < rgb_threshold[0]) | (image[:,:,1] < rgb_threshold[1]) | (image[:,:,2] < rgb_threshold[2])

color_select[pixels] = [0,0,0]

#display the image
plt.imshow(color_select)
plt.show()




