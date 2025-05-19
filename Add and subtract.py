import cv2
import numpy as np

img1=cv2.resize(cv2.imread("cabin.jpg"),(500,500))
img2=cv2.resize(cv2.imread("planet.jpg"),(500,500))
img3=cv2.imread("pikachu.png")

kernel=np.ones((5,5),np.uint8)

added=cv2.addWeighted(img1,0.5,img2,0.5,0)
subbed=cv2.subtract(img1,img2)
eroded=cv2.erode(img3,kernel)

gaussian=cv2.GaussianBlur(img3,(7,7),0)
median=cv2.medianBlur(img3,5)
bilateral=cv2.bilateralFilter(img3,9,75,75)

solidColour=cv2.copyMakeBorder(img3,10,10,10,10,cv2.BORDER_CONSTANT,value=(255,0,225))
reflected=cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_REFLECT)

"""cv2.imshow("Weighted addition",added)
cv2.imshow("Subtraction",subbed)
cv2.imshow("Uneroded",img3)
cv2.imshow("Erosion",eroded)"""

"""cv2.imshow("Gaussian blur",gaussian)
cv2.imshow("Median blur",median)
cv2.imshow("Bilateral blur",bilateral)"""

cv2.imshow("Solid colour border",solidColour)
cv2.imshow("Reflected border",reflected)

cv2.waitKey(0)
cv2.destroyAllWindows()
