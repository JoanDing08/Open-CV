import cv2,sys,os,numpy
size=4
haar="haarcascade_frontalface_default.xml"
dataset="dataset"

print("Recognising face, please remain in sufficient lighting...")

(imgs,labels,names,id)=([],[],{},0)

for (subdirs,dirs,files) in os.walk(dataset):
  for subdir in dirs:
    names[id]=subdir
    subpath=os.path.join(dataset,subdir)

    for filename in os.listdir(subpath):
      path=subpath+"/"+filename
      label=id
      imgs.append(cv2.imread(path,0))
      labels.append(int(label))
    
    id+=1

(width,height)=(130,100)
(imgs,labels)=[numpy.array(lis) for lis in [imgs,labels]]

model=cv2.face.LBPHFaceRecognizer_create()
model.train(imgs,labels)

face_cascade=cv2.CascadeClassifier(haar)
webcam=cv2.VideoCapture(0)

while True:
  (_,img)=webcam.read()
  grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  faces=face_cascade.detectMultiScale(grey,1.3,5)

  for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)
    face=grey[y:y+h,x:x+w]
    resized=cv2.resize(face,(width,height))
    prediction=model.predict(resized)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

    if prediction[1]<500:
      cv2.putText(img,"% s - %.0f" % (names[prediction[0]],prediction[1]),(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(255,100,255))
    else:
      cv2.putText(img,"not recognised",(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0))
  
  cv2.imshow("openCV",img)
  key=cv2.waitKey(10)
  if key==32:
    break
