import cv2

img =cv2.imread("C:\\Users\\gnane\\Pictures\\KKK.jpg")
blur_image = cv2.GaussianBlur(img,(15,15),10)

cv2.imwrite('blur_image.jpg', blur_image)