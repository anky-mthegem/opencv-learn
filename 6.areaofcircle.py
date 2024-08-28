import cv2
import numpy as np
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
        #cv2.imshow("CAMERA DI VIDEO",color)
        #out_color.write(frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
        if circles is not None:
         circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw the circle
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
            
            # Calculate the area of the circle
            area = 3.14159 * (i[2] ** 2)
            print(f"Circle Area: {area:.2f}")
            
            # Display circle coordinates and area
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, f"X: {i[0]}, Y: {i[1]}, Radius: {i[2]}", (10, 20), font, 0.5, (0, 255, 0), 2)
            cv2.putText(frame, f"Area: {area:.2f}", (10, 40), font, 0.5, (0, 255, 0), 2)
    
    # Display the output
    cv2.imshow('Circle Detection', frame)
    k = cv2.waitKey(1)
    if k == ord("e"):
            break
vid.release()
cv2.destroyAllWindows()