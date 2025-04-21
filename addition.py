import cv2
import numpy as np

img1=cv2.imread("umbrella.webp",1)
resized=cv2.resize(img1,(600,600))
cv2.imshow("Resized image",resized)

img2=cv2.imread("cabin.jpg",1)
img3=cv2.imread("planet.jpg",1)

"""weightedadd=cv2.addWeighted(img2,0.5,img3,0.7,0)
sub=cv2.subtract(img2,img3)
cv2.imshow("Weighted addition",weightedadd)
cv2.imshow("subtracted",sub)
"""

gaussian=cv2.GaussianBlur(resized,(5,5),0)
median=cv2.medianBlur(resized,7)
bilateral=cv2.bilateralFilter(resized,9,150,150)
cv2.imshow("Gaussian Blur",gaussian)
cv2.imshow("Median Blur",median)
cv2.imshow("Bilateral Blur",bilateral)

border1=cv2.copyMakeBorder(resized,10,10,10,10,cv2.BORDER_CONSTANT,value=(255,0,250))
border2=cv2.copyMakeBorder(resized,50,50,20,20,cv2.BORDER_REFLECT,value=1)

cv2.imshow("Border image",border1)
cv2.imshow("Reflect Border",border2)

cv2.waitKey(0)
cv2.destroyAllWindows()
