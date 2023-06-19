import cv2

img = cv2.imread("C:\\Users\\gnane\\Pictures\\KKK.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

cv2.imwrite('Canny_Edges_3rd.jpg', edges)