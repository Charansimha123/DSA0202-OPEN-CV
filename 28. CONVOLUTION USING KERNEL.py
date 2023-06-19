import cv2
import numpy as np
img = cv2.imread("C:\\Users\\gnane\\Pictures\\KKK.jpg")

kernel = np.array([[-1,-1,-1],
                   [-1,9,-1],
                   [-1,-1,-1]])

sharpned_img = cv2.filter2D(img, -1, kernel)

cv2.imshow('input image', img)
cv2.imshow('convolutional image', sharpned_img)
cv2.waitkey(0)
cv2.destroyAllWindows()