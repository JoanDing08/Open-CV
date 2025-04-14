import cv2
import numpy as np

load=cv2.imread("umbrella.webp")
print(load.shape)


#convert img to rgb

b,g,r=cv2.split(load)

print(b.shape)

cv2.imshow("Red",r)
cv2.imshow("Green",g)
cv2.imshow("Blue",b)
cv2.imshow("Original",load)

cv2.waitKey(0)
cv2.destroyAllWindows()
