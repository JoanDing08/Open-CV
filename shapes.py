import cv2
import numpy as np

img=cv2.imread("pikachu.png")

start_point1=(0,0)
end_point1=(100,100)
colour1=(0,225,0)
thickness1=-2

rect=cv2.rectangle(img,start_point1,end_point1,colour1,thickness1)

coords=(120,220)
radius=50
colour2=(225,0,200)
thickness2=-1

circle=cv2.circle(img,coords,radius,colour2,thickness2)

start_point2=(300,300)
end_point2=(600,300)
colour3=(0,140,255)
thickness3=10

line=cv2.line(img,start_point2,end_point2,colour3,thickness3)

font=cv2.FONT_HERSHEY_SIMPLEX
scale=1
colour4=(200,255,0)
thickness4=3
origin=(200,200)

text=cv2.putText(img,"Pikachu",origin,font,scale,colour4,thickness4)
cv2.imshow("Text",text)

cv2.waitKey(0)
cv2.destroyAllWindows()
