import cv2

img1 = cv2.imread("C:\Users\amanr\Downloads\cv_test1.jpeg")            
print(img1)
cv2.imshow("original",img1)
cv2.waitkey()
cv2.destroyAllWindow()
