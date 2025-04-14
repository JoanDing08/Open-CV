import cv2
import numpy as np

colour1=np.array([255,0,255])
colour2=np.array([0,130,255])

img1=np.full((300,300,3),colour1,dtype=np.uint8)
img2=np.full((300,300,3),colour2,dtype=np.uint8)

add=cv2.add(img1,img2)
sub=cv2.subtract(img1,img2)

result=np.concatenate((img1,img2,add,sub),axis=1)
cv2.imshow("result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
