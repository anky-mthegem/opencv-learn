#using pytube and youtube-dl library 
#playing MOOSA JAtt from https://www.youtube.com/watch?v=n_FCrCQ6-bA
#try later. Didnt work till 28-08-2024


import cv2
from pytube import YouTube
import youtube_dl
link = YouTube("https://youtu.be/n_FCrCQ6-bA?si=mWdeNOx8WffvwwmP")
data = link.streams.first()
data.download()
file = data.default_filename
vid = cv2.VideoCapture(file)

while vid.isOpened():
    ret,frame = vid.read()
    if ret == True:
        #color = cv2.resize(frame,(700,450))
        cv2.imshow("SIDHU MOOSE WALA",frame)

        k = cv2.waitKey(1)
    if k == ord("e"):
            break
vid.release()
cv2.destroyAllWindows()