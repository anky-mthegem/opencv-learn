import cv2
import pytesseract
#from gtts import gTTS #Trying text to speech 
#from playsound import playsound #Ding Dong playing sounds

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Initialize camera
ipcamera = "http://192.168.137.124:8080/video"
cap = cv2.VideoCapture(0)
cap.open(ipcamera) 

while True:
    # Capture frame
    ret, frame = cap.read()
    
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (1280, 720))

    # Perform OCR
    text = pytesseract.image_to_string(gray)
    boxes = pytesseract.image_to_boxes(gray)

    # Draw bounding boxes around text
    for a in boxes.splitlines():
     a = a.split()
     x, y = int(a[1]), int(a[2])
     w, h = int(a[3]), int(a[4])
     cv2.rectangle(frame, (x, frame.shape[0] - y - h), (x + w, frame.shape[0] - y), (255, 0, 0), 1)

    # Display text
    cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display frame
    cv2.imshow('Frame', frame)
    print(text)

    # Exit on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()