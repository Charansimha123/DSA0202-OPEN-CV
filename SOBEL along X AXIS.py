import cv2
import numpy as np

img = cv2.imread("C:\\Users\\gnane\\Pictures\\KKK.jpg", 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

cv2.imshow('image', img)
cv2.imshow('sobelx', sobelx)

cv2.waitKey(0)
cv2.destroyAllWindows()