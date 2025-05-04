import cv2
import numpy as np

img=cv2.imread("blocks.jpg")

(rows,cols)=img.shape[:2]
m=cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
rotated=cv2.warpAffine(img,m,(cols,rows))
result=("rotated.jpg",rotated)

cv2.imshow("result",rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
