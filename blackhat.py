import cv2

filtersize =(3, 3)
Kernel = cv2.getStructuringElement(cv2.MORPH_RECT,filtersize)


input_image = cv2.imread("C:\\Users\\gnane\\Pictures\\KKK.jpg")
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

blackchat_img = cv2.morphologyEx(input_image, cv2.MORPH_BLACKHAT,Kernel)

cv2.imwrite("original.png", input_image)
cv2.imwrite("blackchat.png", blackchat_img)