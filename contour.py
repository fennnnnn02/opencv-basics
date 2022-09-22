import cv2 # Import OpenCV
import numpy as np # Import NumPy
from rembg import remove

# Read in the image as grayscale - Note the 0 flag
im = cv2.imread('output.png')

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

#ret, thresh = cv2.threshold(im, 1, 255, cv2.THRESH_OTSU)

# Run findContours - Note the RETR_EXTERNAL flag
# Also, we want to find the best contour possible with CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(imgray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Create an output of all zeroes that has the same shape as the input
# image
out = np.zeros_like(im)

# On this output, draw all of the contours that we have detected
# in white, and set the thickness to be 3 pixels


cv2.drawContours(im, contours, -1, (0,255,0), 2)
#cv2.drawContours(out, contours, -1, (255,0,0), 2)

# Spawn new windows that shows us the donut
# (in grayscale) and the detected contour
im = remove(im)
cv2.imshow('Donut', im) 

cv2.imwrite('output.jpg',im)

# Wait indefinitely until you push a key.  Once you do, close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()