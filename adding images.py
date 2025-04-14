import cv2
import numpy as np

load1=cv2.imread("cabin.jpg")
load2=cv2.imread("planet.jpg")

combine=cv2.addWeighted(load1,0.7,load2,0.4,0)

cv2.imshow("added images",combine)

cv2.waitKey(0)
cv2.destroyAllWindows()