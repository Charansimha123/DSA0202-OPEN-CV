import cv2
import numpy as np

img = cv2.imread('C:\\Users\\gnane\\Pictures\\KKK.jpg')

rows, cols = img.shape[:2]
M = np.float32([[1, 1, 1000], [0, 1, 500]])

affine_img = cv2.warpAffine(img, M, (cols, rows))

cv2.imwrite('Affined_Transformed.jpg',affine_img)