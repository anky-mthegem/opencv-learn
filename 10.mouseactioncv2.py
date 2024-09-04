import cv2
import numpy as np

# Initialize camera

ipcamera = "http://192.168.137.175:8080/video"
cap = cv2.VideoCapture(0)
cap.open(ipcamera)

# Set initial zoom level
zoom_level = 1.0

# Define mouse callback function
def mouse_callback(event, x, y, flags, params):
    global zoom_level
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:  # Mouse wheel scrolled up
            zoom_level += 0.1
        else:  # Mouse wheel scrolled down
            zoom_level -= 0.1
        zoom_level = max(0.1, min(zoom_level, 10))  # Limit zoom level

# Create window and set mouse callback
cv2.namedWindow("Video")
cv2.setMouseCallback("Video", mouse_callback)

while True:
    # Capture frame
    ret, frame = cap.read()
    
    if not ret:
        break

    # Calculate zoomed ROI
    height, width, _ = frame.shape
    center_x = width // 2
    center_y = height // 2
    roi_width = int(width / zoom_level)
    roi_height = int(height / zoom_level)
    roi_x = center_x - roi_width // 2
    roi_y = center_y - roi_height // 2
    
    # Apply zoom
    zoomed_frame = cv2.resize(frame[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width], (width, height))

    
    # Display zoomed frame
    cv2.imshow("Video", zoomed_frame)
    #cv2.resizeWindow(600,700,zoomed_frame)
    
    # Exit on key press
    k = cv2.waitKey(1) 
    if k == ord("e"):
        break

# Release camera and close window
cap.release()
cv2.destroyAllWindows()