import cv2
import numpy as np
 
cap = cv2.VideoCapture("C:\\Users\\gnane\\Pictures\\Camera Roll\\WIN_20230503_13_11_21_Pro.mp4")
 
while True:
     
    ret, frame = cap.read()
    pts1 = np.float32([[0, 260], [640, 260],[0, 400], [640, 400]])
    pts2 = np.float32([[0, 0], [400, 0],[0, 640], [400, 640]])
     
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (500, 600))
     
    cv2.imshow('original video', frame) 
    cv2.imshow('perspective video', result) 
 
    if cv2.waitKey(24) == 27:
        break
 
cap.release()
cv2.destroyAllWindows()