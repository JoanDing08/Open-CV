import cv2
import numpy as np

img=cv2.imread("pikachu.png")

(rows,cols)=img.shape[:2]
m=cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
res=cv2.warpAffine(img,m,(cols,rows))

result=cv2.imwrite("result.png",res)

cv2.imshow("result",res)

edges=cv2.Canny(img,100,200)
cv2.imwrite("results.jpg",edges)
cv2.imshow("",edges)


cv2.waitKey(0)
cv2.destroyAllWindows()
