import cv2
import numpy as np

#Use some of own images to create a family collage
#Introduce tilted, grayscale or inverted images in the collage

img1=cv2.cvtColor(cv2.resize(cv2.imread("rose.jpg"),(230,200)),cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(cv2.resize(cv2.imread("strawberries.jpg"),(230,200)),cv2.COLOR_BGR2GRAY)
img3=cv2.cvtColor(cv2.resize(cv2.imread("almonds.jpg"),(230,200)),cv2.COLOR_BGR2GRAY)
img4=cv2.cvtColor(cv2.resize(cv2.imread("blackberries.jpg"),(230,200)),cv2.COLOR_BGR2GRAY)
img5=cv2.cvtColor(cv2.resize(cv2.imread("plum blossoms.jpg"),(230,200)),cv2.COLOR_BGR2GRAY)
img6=cv2.cvtColor(cv2.resize(cv2.imread("apples.jpg"),(230,200)),cv2.COLOR_BGR2GRAY)
img7=cv2.cvtColor(cv2.resize(cv2.imread("peaches.jpg"),(230,200)),cv2.COLOR_BGR2GRAY)
img8=cv2.cvtColor(cv2.resize(cv2.imread("loquat.jpg"),(230,200)),cv2.COLOR_BGR2GRAY)
img9=cv2.cvtColor(cv2.resize(cv2.imread("cherries.jpg"),(230,200)),cv2.COLOR_BGR2GRAY)

collection1=np.vstack((img1,img2,img3))
collection2=np.vstack((img4,img5,img6))
collection3=np.vstack((img7,img8,img9))

collage=np.concatenate((collection1,collection2,collection3),axis=1)

cv2.imshow("Rosaceae family",collage)

cv2.waitKey(0)
cv2.destroyAllWindows()
