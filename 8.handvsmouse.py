import cv2 #pretty common thing
import mediapipe as mp #mediapipe library for hand tracking
import pyautogui #for controling mouse 
import ctypes #for adding window transparent feature
offset = 300 
#ipcamera = "http://192.168.137.13:8080/video" #just in-case if ip camera is required to connect
cap = cv2.VideoCapture(0)
#cap.open(ipcamera) #send ipcamera to cap
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_x = 0
index_y = 0
while True:
    ret , frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand) 
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y

                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 30:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    elif 70 < abs(index_y - thumb_y) < 200:
                        pyautogui.moveTo(index_x + offset, index_y + offset)
    cv2.imshow('Mouse vali Window', frame)
    #hwnd = ctypes.windll.user32.FindWindowW(None, 'Mouse vali Window')
    #ctypes.windll.user32.SetWindowLongW(hwnd, -20, 0x00080000 | 0x00000020)  # WS_EX_LAYERED | WS_EX_TRANSPARENT
    #ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, 128, 2)  # 50% transparency
    k = cv2.waitKey(1)
    if k == ord("e"):
            break
cap.release()
cv2.destroyAllWindows()