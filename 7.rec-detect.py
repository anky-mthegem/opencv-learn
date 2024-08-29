import cv2  
import numpy as np  
 
camera_height = 240 
 
P1Default = 8     # Blur Amount  
P2Default = 90    # Canny threshold1  
P3Default = 120   # Canny threshold2  
P4Default = 2     # Dilation para1  
P5Default = 2     # Dilation para2  
P6Default = 3000   # Area Threshold  
 
def main():  
    # Start video capture from the camera  
    ipcamera = "http://192.168.137.13:8080/video"
    cap = cv2.VideoCapture(0)
    cap.open(ipcamera)
    print(cap)
      
 
    def onTrackbarChange1(trackbarValue):  
        pass  
 
    # Create a window and trackbars  
    cv2.namedWindow('Original')  
    cv2.namedWindow('Gray')  
    cv2.namedWindow('Blur')  
    cv2.namedWindow('Canny') 
    cv2.namedWindow('Dialated')  
    cv2.namedWindow('Final')  
    #cv2.resizeWindow('Final', 400, 400)
    cv2.createTrackbar('P1', 'Blur', P1Default, 200, onTrackbarChange1) 
    cv2.resizeWindow('Blur', 400, 400) 
    cv2.createTrackbar('P2', 'Canny', P2Default, 255, onTrackbarChange1)  
    cv2.createTrackbar('P3', 'Canny', P3Default, 255, onTrackbarChange1)  
    cv2.resizeWindow('Canny', 400, 400)
    cv2.createTrackbar('P4', 'Dialated', P4Default, 10, onTrackbarChange1)  
    cv2.createTrackbar('P5', 'Dialated', P5Default, 10, onTrackbarChange1) 
    cv2.resizeWindow('Dialated', 400, 400) 
    cv2.createTrackbar('P6', 'Final', P6Default, 5000, onTrackbarChange1)  
    cv2.resizeWindow('Final', 400, 400)
 
    while True:  
        ret, frame = cap.read()  
        if not ret:  
            print("Failed to capture image")  
            break  
 
        # Show the frame  
        color = cv2.resize(frame,(700,450))
        cv2.imshow('Original', color)  
 
        # Check for key presses  
        key = cv2.waitKey(1) & 0xFF  
        if key == ord('c'):  # Press 'c' to capture the frame  
            process_frame(frame)  
        elif key == ord('q'):  # Press 'q' to quit  
            break  
 
    # Release resources  
    cap.release()  
    cv2.destroyAllWindows()  
 
def process_frame(frame):  
 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
 
    # Apply Blur  
    P1 = cv2.getTrackbarPos('P1', 'Blur')  
    if P1 % 2 == 0:  
        P1 += 1  
    blurred = cv2.medianBlur(gray, P1)  
 
    # Apply Canny edge detection  
    P2 = cv2.getTrackbarPos('P2', 'Canny')  
    P3 = cv2.getTrackbarPos('P3', 'Canny')  
    edged = cv2.Canny(blurred, P2, P3)  
 
    # Image Dilation  
    P4 = cv2.getTrackbarPos('P4', 'Dialated')  
    P5 = cv2.getTrackbarPos('P5', 'Dialated')  
    kernel = np.ones((P4, P5))  
    imgdil = cv2.dilate(edged, kernel, iterations=1)  
 
    contours, _ = cv2.findContours(imgdil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  
    P6 = cv2.getTrackbarPos('P6', 'Final')  
    panel_detected = False  
 
    for contour in contours:  
        rect = cv2.minAreaRect(contour)  
        box = cv2.boxPoints(rect)  
        box = np.intp(box)  
 
        width, height = rect[1]  
        scale_factor = camera_height / 656.2  
        length_cm = height * scale_factor  
        width_cm = width * scale_factor  
        area = length_cm * width_cm  
       
 
        center_x, center_y = map(int, rect[0])  
        CX = round(center_x * scale_factor, 2)  
        CY = round(center_y * scale_factor, 2)  
 
        if area > P6:  
            panel_detected = True  
            print(length_cm,"*",width_cm,"=",area)
            cv2.drawContours(frame, [box], 0, (0, 255, 0), 1)  
            cv2.putText(frame, f'L: {length_cm:.2f} mm, W: {width_cm:.2f} mm',  
                        (box[0][0], box[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)  
            cv2.putText(frame, f'(X: {CX}, Y: {CY})',  
                        (box[0][0], box[0][1] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)  
 
    # Show the processed result 
    cv2.imshow('Gray', gray)
    cv2.imshow('Blur', blurred)  
    cv2.imshow('Canny', edged)  
    cv2.imshow('Dialated',imgdil)
    cv2.imshow('Final', frame)  
 
if __name__ == "__main__":  
    main()
 