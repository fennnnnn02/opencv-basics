import cv2
import numpy as np
from rembg import remove

im = cv2.imread("images/1.1-input.jpg",cv2.IMREAD_ANYCOLOR)
imS = cv2.resize(im, (960, 540))   

#cv2.imshow("image",imS)
#cv2.moveWindow("image", 250, 100)


# Select ROI
r = cv2.selectROI(imS) 
print(r)
# Crop image
imCrop = imS[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
cv2.imshow("crop",imCrop)

output_path = 'images/output.png'

output = remove(imCrop)
cv2.imwrite(output_path, output)

cv2.waitKey(0)
cv2.destroyAllWindows()
