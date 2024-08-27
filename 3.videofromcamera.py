import cv2

vid = cv2.VideoCapture(0)
print(vid)
while vid.isOpened():
    ret,frame = vid.read()
    if ret == True:
        color = cv2.resize(frame)
