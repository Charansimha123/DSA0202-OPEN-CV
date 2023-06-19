import cv2

img = cv2.imread("C:\\Users\\gnane\\Pictures\\KKK.jpg")

grey_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

cv2.imwrite("grey_img.jpg",grey_img)