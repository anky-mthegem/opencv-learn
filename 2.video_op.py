import cv2
video = cv2.VideoCapture("C:\\Users\\amanr\\Downloads\\VSCODE_FILES\\M app\\OpenCV-learn\\Bobbin.mp4")
print("video",video)

while True:
    ret,frame = video.read()
    cv2.imshow("frame",frame)
cv2.waitKey(15000)
video.release()
cv2.destroyAllWindows()
