import cv2
import numpy as np

img=cv2.imread("pikachu.png")
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.blur(grey,(3,3))


detect_circle=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=1,maxRadius=40)

if detect_circle is not None:
  detected_circle=np.int16(np.around(detect_circle))
  for i in detected_circle[0,:]:
    x,y,r=i[0],i[1],i[2]
    cv2.circle(img,(x,y),r,(20,140,55),2)
    cv2.circle(img,(x,y),1,(12,221,43),3)
    cv2.imshow("Detected circles",img)
    cv2.waitKey(0)
  cv2.destroyAllWindows()


param=cv2.SimpleBlobDetector_Params()

param.filterByArea=True
param.minArea=100
param.filterByCircularity=True
param.minCircularity=0.9
param.filterByConvexity=True
param.minConvexity=0.2
param.filterByInertia=True
param.minInertiaRatio=0.01

detect_blob=cv2.SimpleBlobDetector_create(param)
keypoints=detect_blob.detect(grey)
blank=np.zeros((1,1))
blob=cv2.drawKeypoints(grey,keypoints,blank,(0,0,225),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

blob_num=len(keypoints)
text="Number of blobs: "+str(blob_num)
cv2.putText(blob,text,(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,225),2)

cv2.imshow("Finding circular blobs only",blob)

cv2.waitKey(0)
cv2.destroyAllWindows()
