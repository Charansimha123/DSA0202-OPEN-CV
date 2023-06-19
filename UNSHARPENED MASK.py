from PIL import image, imageFilter
import cv2
im1 = image.open("C:\\Users\\gnane\\Pictures\\KKK.jpg")

im2 = im1.filter(imageFilter.unsharpmask(radius = 3, percent = 200, threshold = 5))

im2.show()