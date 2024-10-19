import cv2

# Open the default camera (index 0)
ipcamera = "http://192.168.137.124:8080/video"
cap = cv2.VideoCapture(0)
cap.open(ipcamera)  # Use 0 for the default camera
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Display the frame
    cv2.imshow('Camera', frame)

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF

    # Save image when 's' is pressed
    if key == ord('s'):
        cv2.imwrite('captured_image.jpg', frame)
        print("Image saved!")

    # Quit when 'q' is pressed
    elif key == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()