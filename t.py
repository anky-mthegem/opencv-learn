import cv2

# Open Android camera
cap = cv2.VideoCapture(0)  # or 2, 3, etc.

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Android Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()