import cv2
import numpy as np

image = cv2.imread("C:\\Users\\gnane\\Pictures\\KKK.jpg")

kernel = np.array([[0, 1, 0],
                   [1, -8, 1],
                   [0, 1, 0]])
sharpened = cv2.filter2D(image, -1, kernel)

cv2.imwrite('original.jpg', image)
cv2.imwrite('sharpened.jpg', sharpened)
