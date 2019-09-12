import cv2
import numpy as np
import time
import os

img = cv2.imread('test_photo/final_s 0.jpg')
mask = np.zeros(img.shape, dtype=np.uint8)
max_loc = (320,240)
circle_radius = 80;
cv2.circle(mask, max_loc, 80, (255, 255, 255), -1, 8, 0)

#cv2.circle(mask,)
# Apply mask (using bitwise & operator)
result_array = img & mask

# Crop/center result (assuming max_loc is of the form (x, y))
result_array = result_array[max_loc[1] - circle_radius:max_loc[1] + circle_radius,
                            max_loc[0] - circle_radius:max_loc[0] + circle_radius, :]
print(result_array)