import cv2
video = cv2.VideoCapture("C:\\Users\\amanr\\Downloads\\VSCODE_FILES\\M app\\OpenCV-learn\\con.mp4")
print("video",video)

while True:
    ret,frame = video.read()
    cv2.imshow("AA CHAKK VIDEO",frame)
    k = cv2.waitKey(30)
    if k == ord("e"):
        break
video.release()
#exit()
cv2.destroyAllWindows()
