import cv2
import numpy as np

img1=cv2.imread("pikachu.png")
cv2.imshow("Original",img1)

img2=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imshow("Greyscale",img2)

#greyscale without library

(row,col)=img1.shape[0:2]
for i in range(row):
  for j in range(col):
    img1[i,j]=sum(img1[i,j])*0.33

cv2.imshow("Greyscale 2",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
