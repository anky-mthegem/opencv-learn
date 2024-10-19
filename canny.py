import cv2

# Open the default camera (index 0)
ipcamera = "http://192.168.137.124:8080/video"
cap = cv2.VideoCapture(0)
cap.open(ipcamera)


# Create windows and sliders
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Canny', cv2.WINDOW_NORMAL)

# Set window sizes
#cv2.resizeWindow('Original', 600, 400)
#cv2.resizeWindow('Canny', 600, 400)

# Move windows to prevent overlap (optional)
#cv2.moveWindow('Original', 100, 50)
#cv2.moveWindow('Canny', 800, 50)

# Initial threshold values
min_threshold = 100
max_threshold = 200

# Create sliders
cv2.createTrackbar('Min Threshold', 'Canny', min_threshold, 255, lambda x: None)
cv2.createTrackbar('Max Threshold', 'Canny', max_threshold, 255, lambda x: None)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Get current threshold values from sliders
    min_threshold = cv2.getTrackbarPos('Min Threshold', 'Canny')
    max_threshold = cv2.getTrackbarPos('Max Threshold', 'Canny')

    # Apply Canny edge detection
    canny = cv2.Canny(gray, min_threshold, max_threshold)

    # Display the original and Canny images
    cv2.imshow('Original', cv2.resize(frame, (600, 400), interpolation=cv2.INTER_CUBIC))
    cv2.imshow('Canny', cv2.resize(canny, (600, 400), interpolation=cv2.INTER_CUBIC))

    # Press 'q' to quit, 's' to save the Canny image
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite('canny_image.jpg', canny)

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
