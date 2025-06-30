import cv2

vid=cv2.VideoCapture("motorway.mp4")
car_casc=cv2.CascadeClassifier("cars.xml")

while True:
  ret,frames=vid.read()
  gray=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
  cars=car_casc.detectMultiScale(gray,1.1,1)

  for (x,y,w,h) in cars:
    cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

  cv2.imshow("Video 2",frames)

  key=cv2.waitKey(10)
  if key==32:
    break
