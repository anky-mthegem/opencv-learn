import cv2

vid = cv2.VideoCapture(0)
print(vid)
while vid.isOpened():
    ret,frame = vid.read()
    if ret == True:
        color = cv2.resize(frame,(700,450))
        cv2.imshow("CAMERA DI VIDEO",color)
        k = cv2.waitKey(1)
    if k == ord("e"):
            break
color.release()
cv2.destroyAllWindows()
