#Homework: detect the number of people in an image

import cv2
import numpy as np

og=cv2.imread("people.jpg")
img=cv2.resize(og,(700,700))

cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
detect_face=cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=13,minSize=(20, 20))

for (x,y,w,h) in detect_face:
  cv2.rectangle(img,(x,y),(x+w,y+h),(220,0,150),1)

people_num=len(detect_face)
text="Number of people: "+str(people_num)
cv2.putText(img,text,(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(170,0,100),2)

cv2.imshow("detecting people",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
