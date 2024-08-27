import cv2
video = cv2.VideoCapture("C:\\Users\\amanr\\Downloads\\VSCODE_FILES\\M app\\OpenCV-learn\\con.mp4")
print("video",video)

while True:
    ret,frame = video.read()
    #frame = cv2.resize(frame,(700,450))
    cv2.imshow("frame",frame)

cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()
