import cv2,numpy,sys,os

haar="haarcascade_frontalface_default.xml"
dataset="dataset"
subdata="jim"
path=os.path.join(dataset,subdata)

if not os.path.isdir(path):
  os.makedirs(path)

(width,height)=(130,100)

cascade=cv2.CascadeClassifier(haar)


webcam=cv2.VideoCapture(1)

count=1
while count<30:
  (ret,img)=webcam.read()
  if not ret:
    print("failed to grab frame from webcam")
    break
  gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  face=cascade.detectMultiScale(gray,1.3,4)
  for(x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+w),(255,0,0),2)
    face=gray[y:y+h,x:x+w]
    size=cv2.resize(face,(w,h))
    cv2.imwrite("%s/%s.png"%(path,count,size))
  count+=1
  cv2.imshow("open cv",img)

  key=cv2.waitKey(10)
  if key==27:
    break

