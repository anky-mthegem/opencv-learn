import cv2

vid = cv2.VideoCapture(0)
print(vid)
while vid.isOpened():
    ret,frame = vid.read()
    if ret == True:
        #color = cv2.resize(frame,(700,450))
        cv2.imshow("CAMERA DI VIDEO",frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("B&B dekho ji",gray)
        k = cv2.waitKey(1)
    if k == ord("e"):
            break
vid.release()
cv2.destroyAllWindows()
