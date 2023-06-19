import cv2
import numpy as np

img = cv2.imread("C:\\Users\\gnane\\Pictures\\IMG20221009110318.jpg", cv2.IMREAD_GRAYSCALE)

laplacian_filter = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

sharpened = cv2.filter2D(img, -1, laplacian_filter)

sharpened_img = cv2.addWeighted(img, 1.5, sharpened, -0.5, 0)

cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image', sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()