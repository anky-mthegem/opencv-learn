#using mobile camera server for trial. Later GIGE camera can be used using ip
import cv2
ipcamera = "http://192.168.137.13:8080/video"
vid = cv2.VideoCapture(0)
vid.open(ipcamera)
print(vid)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out_color = cv2.VideoWriter('output_color.avi', fourcc, 20.0, (640, 480)) #use fourcc function to make a output file name output_color
#out_gray = cv2.VideoWriter('output_gray.avi', fourcc, 20.0, (640, 480),0) # require to pass zero after frame size to let function know that the frames recieved are gray scale
while vid.isOpened():
    ret,frame = vid.read()
    if ret == True:
        color = cv2.resize(frame,(700,450))
        cv2.imshow("CAMERA DI VIDEO",color)
        #out_color.write(frame)
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow("B&B dekho ji",gray)
        #out_gray.write(gray)
        k = cv2.waitKey(1)
    if k == ord("e"):
            break
vid.release()
cv2.destroyAllWindows()