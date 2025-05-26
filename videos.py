import cv2
import numpy as np
import time

video=cv2.VideoCapture("test video.mp4")

time.sleep(1)
count=0
bg=0

for i in range(60):
  return_val,bg=video.read()
  if return_val==False:
    continue

bg=np.flip(bg,axis=1)

while video.isOpened():
  return_val,img=video.read()
  if not return_val:
    break
  count+=1
  img=np.flip(img,axis=1)
  hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  lowerRed=np.array([100,40,40])
  upperRed=np.array([100,255,255])
  mask1=cv2.inRange(hsv,lowerRed,upperRed)
  lowerRed=np.array([155,40,40])
  uppperRed=np.array([180,255,255])
  mask2=cv2.inRange(hsv,lowerRed,upperRed)
  mask1=mask1+mask2
  mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
  mask1=cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations=1)
  mask2=cv2.bitwise_not(mask1)
  res1=cv2.bitwise_and(bg,bg,mask=mask1)
  res2=cv2.bitwise_and(img,img,mask=mask2)
  result=cv2.addWeighted(res1,0.2,res2,0.5,0)
  cv2.imshow("result",result)

  k=cv2.waitKey(10)
  if k==27:
    break
