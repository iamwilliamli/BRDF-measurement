import numpy as np
import cv2
from matplotlib import pyplot as plt

img2 = cv2.imread('/Users/William/BRDF/test_photo/final\ 0.jpg')
img1 = cv2.imread('/Users/William/BRDF/test_photo/test\ 10.jpg')

#dst = cv2.fastNlMeansDenoisingColored(img1,None,10,10,7,21)

#cv2.addWeighted(img1,0.5,img2,0.5,0)

#img3 = img1*255
#img4 = (img2)*255
#img5 = (dst)*255


plt.subplot(231),plt.imshow(img1)
plt.subplot(232),plt.imshow(img2)
plt.subplot(233),plt.imshow(img3)
plt.subplot(234),plt.imshow(img4)
#plt.subplot(235),plt.imshow(img5)

plt.show()
