import cv2
import numpy as np

img = cv2.imread('C:\\Users\\gnane\\Pictures\\Camera Roll\\WIN_20230503_13_11_21_Pro.mp4',0)

edges = cv2.Canny(img,100,200)

cv2.imshow('Edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()