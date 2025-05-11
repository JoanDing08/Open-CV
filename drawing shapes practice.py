import cv2
import numpy as np

#homework, draw start/heart on image

img=cv2.imread("blocks.jpg")

colour=(0,0,0)
thickness=25

start_point1=(50,20)
end_point1=(100,82)

start_point2=(100,82)
end_point2=(20,66)

start_point3=(20,66)
end_point3=(105,35)

start_point4=(105,35)
end_point4=(50,100)

start_point5=(50,100)
end_point5=(50,20)


line1=cv2.line(img,start_point1,end_point1,colour,thickness)
line2=cv2.line(img,start_point2,end_point2,colour,thickness)
line3=cv2.line(img,start_point3,end_point3,colour,thickness)
line4=cv2.line(img,start_point4,end_point4,colour,thickness)
line5=cv2.line(img,start_point5,end_point5,colour,thickness)

cv2.imshow("Star",line1)
cv2.imshow("Star",line2)
cv2.imshow("Star",line3)
cv2.imshow("Star",line4)
cv2.imshow("Star",line5)

cv2.waitKey(0)
cv2.destroyAllWindows()
