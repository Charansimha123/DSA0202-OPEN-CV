import cv2
import numpy as np
img = cv2.imread("C:\\Users\\gnane\\Pictures\\KKK.jpg")

Kernel = np.ones((5, 5), np.uint8)

opening = cv2.morphologyEx(img, Kernel, iterations=1)

cv2.imshow('original', img)
cv2.imshow('opened', opening)
cv2.waitkey(0)
cv2.destroyAllWindows()