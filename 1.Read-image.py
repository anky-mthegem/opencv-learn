import cv2

# Read the image
image = cv2.imread("C:\\Users\\amanr\\Downloads\\VSCODE_FILES\\M app\\OpenCV-learn\\cv_test1.jpeg",1)

# Check if the image is loaded properly
if image is None:
    print("MAMA HEER DYA. PHOTO KITHE AA")
else:
    # Resize the image to 600x400
    resized_image = cv2.resize(image, (600, 400))

    # Display the resized image
    cv2.imshow('Dekhla photo', resized_image)
    k = cv2.waitKey(0)
    if k==ord("s"):
        cv2.imwrite("C:\\Users\\amanr\\Downloads\\VSCODE_FILES\\M app\\OpenCV-learn\\cv_test1_s.jpeg",image)
    else:
     cv2.destroyAllWindows()
    #ajj ka kaam khatam
    #successfully read image on 26/08/2024