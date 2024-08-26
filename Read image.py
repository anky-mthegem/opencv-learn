import cv2

# Read the image
image = cv2.imread("C:\\Users\\amanr\\Downloads\\cv_test1.jpeg")

# Check if the image is loaded properly
if image is None:
    print("MAMA HEER DYA. PHOTO KITHE AA")
else:
    # Resize the image to 600x400
    resized_image = cv2.resize(image, (600, 400))

    # Display the resized image
    cv2.imshow('Resized Image', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()