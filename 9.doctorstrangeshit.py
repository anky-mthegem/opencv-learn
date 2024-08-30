import cv2
import numpy as np

# Initialize video capture
cap = cv2.VideoCapture(0)

# Set circle properties
circle_radius = 20
circle_color = (255, 255, 255)  # White
sparkle_radius = 5
sparkle_color = (0, 255, 255)  # Yellow

# Hand detection variables
hand_detected = False
hand_center = (0, 0)
prev_hand_center = (0, 0)

while True:
    # Read frame from camera
    ret, frame = cap.read()
    
    # Flip frame horizontally (mirror effect)
    frame = cv2.flip(frame, 1)
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Detect circles using Hough transform
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=10, maxRadius=0)
    
    # Check if circles detected
    if circles is not None:
        # Get hand center coordinates
        hand_center = (circles[0][0][0], circles[0][0][1])
        
        # Draw circle around hand
        cv2.circle(frame, hand_center, circle_radius, circle_color, 2)
        
        # Draw sparkling circles
        for i in range(5):
            sparkle_x = hand_center[0] + int(np.cos(i * np.pi / 2.5) * circle_radius)
            sparkle_y = hand_center[1] + int(np.sin(i * np.pi / 2.5) * circle_radius)
            cv2.circle(frame, (sparkle_x, sparkle_y), sparkle_radius, sparkle_color, -1)
        
        # Update hand detection flag
        hand_detected = True
    else:
        hand_detected = False
    
    # Display frame
    cv2.imshow('Sparkling Hands', frame)
    
    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
