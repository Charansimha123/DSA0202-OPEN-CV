import cv2
import numpy as np

img = cv2.imread('C:\\Users\\gnane\\Pictures\\KKK.jpg',0)

sobel_y = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=5)

cv2.imshow('sobel_y',sobel_y)
cv2.waitKey(0)
cv2.destroyAllWindows()