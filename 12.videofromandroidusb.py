import cv2
from PyAndroid import Android
import numpy as np

# Connect to Android device
droid = Android()

# Initialize camera
camera_id = 0  # Rear camera (default)
droid.cameraStart(camera_id)

# Set camera resolution (optional)
droid.cameraSetResolution(640, 480)

while True:
    # Capture frame from camera
    frame = droid.cameraGetFrame()

    # Convert frame to OpenCV format
    frame = cv2.imdecode(np.frombuffer(frame, np.uint8), cv2.IMREAD_COLOR)

    # Display frame
    cv2.imshow('Android Camera', frame)

    # Exit on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close windows
droid.cameraStop()
cv2.destroyAllWindows()