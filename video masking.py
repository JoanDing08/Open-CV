import cv2
import numpy as np
import time

#mask a video with green instead of red

video=cv2.VideoCapture("test video 2.mp4")

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
  lowerGreen=np.array([36,200,200])
  upperGreen=np.array([36,255,255])
  mask1=cv2.inRange(hsv,lowerGreen,upperGreen)
  lowerGreen=np.array([85,200,200])
  upperGreen=np.array([100,255,255])
  mask2=cv2.inRange(hsv,lowerGreen,upperGreen)
  mask1=mask1+mask2
  mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
  mask1=cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations=1)
  mask2=cv2.bitwise_not(mask1)
  res1=cv2.bitwise_and(bg,bg,mask=mask1)
  res2=cv2.bitwise_and(img,img,mask=mask2)
  result=cv2.addWeighted(res1,0.2,res2,0.5,0)
  cv2.imshow("result",result)

  k=cv2.waitKey(10)
  if k==32: #k=32 is the space key
    break
