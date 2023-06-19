import cv2
import numpy as np

def high_boost_filter(image, boost_factor):
    kernel_size = 3
    blur_factor = (kernel_size - 1) / 2
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size ** 2)
    blur_image = cv2.filter2D(image, -1, kernel)
    mask = boost_factor * image - blur_factor
    return mask

image = cv2.imread('C:\\Users\\gnane\\Pictures\\Camera Roll\\WIN_20230503_13_11_21_Pro.mp4')
sharpened_image = high_boost_filter(image, 1.5)
cv2.imwrite('sharpened_imagee.jpg', sharpened_image)