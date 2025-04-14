import cv2

load1=cv2.imread("pikachu.png",cv2.IMREAD_COLOR)
load2=cv2.imread("pikachu.png",0)


cv2.imshow("pikachu colour",load1)
cv2.imshow("pikachu greyscale",load2)

b,g,r=cv2.split(load1)

cv2.imshow("pikachu blue",b)
cv2.imshow("pikachu green",g)
cv2.imshow("pikachu red",r)

cv2.waitKey(0)
cv2.destroyAllWindows()