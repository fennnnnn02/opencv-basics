import cv2
import numpy as np

im = cv2.imread("output.png",cv2.IMREAD_ANYCOLOR)
#imS = cv2.resize(im, (960, 540))   

blur = cv2.GaussianBlur(im,(5,5),0)

cv2.imshow("blur",blur)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
 
cv2.imshow('Grayscale',gray)

cv2.imwrite('output.png',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

