from PIL import Image
import cv2
from rembg import remove
  
# Opening the primary image (used in background)

from PIL import Image
  
# Opening the primary image (used in background)
img1 = Image.open(r"images/1.1-input.jpg")
img1 = img1.resize((960,540),Image.ANTIALIAS)
  
# Opening the secondary image (overlay image)
img2 = Image.open(r"output.png")
  
# Pasting img2 image on top of img1 
# starting at coordinates (0, 0)
img1.paste(img2, (192,180), mask = img2)
  
# Displaying the image
img1.show()