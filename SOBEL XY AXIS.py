import cv2
import numpy as np

img = cv2.imread("C:\\Users\\gnane\\Pictures\\IMG20221009110318.jpg", cv2.IMREAD_GRAYSCALE)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

sobel_combined = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

cv2.imshow('Sobel Edge Detection', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()