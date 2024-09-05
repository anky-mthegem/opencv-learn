import cv2
import numpy as np


def cross(x):
    pass


img = np.zeros((300,512),np.uint8)
cv2.namedWindow("color picker")


#create switch
s1 = "0:OFF/1:ON"
cv2.createTrackbar(s1,"color picker",0,1,cross)


#for rgb

cv2.createTrackbar("r","color picker",0,255,cross)
cv2.createTrackbar("g","color picker",0,255,cross)
cv2.createTrackbar("b","color picker",0,255,cross)

while True:
    cv2.imshow("color picker",img)
    k = cv2.waitKey(1)
    if k==ord("e"): #27 is keyword for esc key pressed
        break

    #get trackbar position
    s = cv2.getTrackbarPos(s1,"color picker")
    r = cv2.getTrackbarPos("r","color picker")
    g = cv2.getTrackbarPos("g","color picker")
    b = cv2.getTrackbarPos("b","color picker")

if s ==0:
        img[:] = 0
else:
        img[:] = [r,g,b]

cv2.destroyAllWindows()


