import cv2
import numpy as np
img = cv2.imread("C:\\Users\\gnane\\Pictures\\KKK.jpg")

kernel = np.ones((5,5), np.uint8)

errosion_img = cv2.erode(img, kernel, iterations=1)

cv2.imwrite('errosion_image.jpg',errosion_img)