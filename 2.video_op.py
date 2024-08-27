import cv2
video = cv2.VideoCapture("C:\\Users\\amanr\\Downloads\\VSCODE_FILES\\M app\\OpenCV-learn\\con.mp4")
print("video",video)

while True:
    ret,frame = video.read()
    #bnb = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("AA CHAKK VIDEO",frame)
    bnb = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("BLACK & WHITE VIDEO DEKHO",bnb)
    k = cv2.waitKey(33)
    if k == ord("e"):
        break
video.release()
#exit()
cv2.destroyAllWindows()
