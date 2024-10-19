import cv2
import numpy as np
 
# Function to capture an image using a connected camera
def capture_image():
    ipcamera = "http://192.168.137.124:8080/video"
    cap = cv2.VideoCapture(ipcamera)  # Use the IP camera directly
    ret, frame = cap.read()
    if ret:
        cap.release()
        return frame
    else:
        cap.release()
        raise Exception("Could not capture image from camera")
 
# Function to apply Canny edge detection
def canny_edge_detection(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, 50, 50)
    return edges
 
# Function to compare two images and calculate similarity percentage
def compare_images(image1, image2):
    difference = cv2.absdiff(image1, image2)
    # Binary thresholding
    threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
    # Calculate similarity based on non-zero pixels in the thresholded image
    similarity = 1 - (cv2.countNonZero(threshold) / (image1.shape[0] * image1.shape[1]))
    return similarity * 100
 
# Path to the base image
base_image_path = "canny_image.jpg"
 
# Step 1: Capture a live image from the camera
captured_image = capture_image()
 
# Step 2: Apply Canny edge detection to the captured image
captured_image_edges = canny_edge_detection(captured_image)
 
# Step 3: Load the base image and ensure it's grayscale
base_image_edges = cv2.imread(base_image_path, cv2.IMREAD_GRAYSCALE)
if base_image_edges is None:
    raise Exception(f"Could not load base image from {base_image_path}")
 
# Step 4: Compare the Canny-processed captured image with the base image
similarity_percentage = compare_images(captured_image_edges, base_image_edges)
print(f"Similarity: {similarity_percentage:.2f}%")
 
# Optional: Display the images for visual confirmation
#cv2.imshow("Captured Image Edges", captured_image_edges)
#cv2.imshow("Base Image Edges", base_image_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
# Step 5: Check similarity threshold and print result
threshold = 90  # Adjust this threshold as needed
 
if similarity_percentage >= threshold:
    print("OK Image")
else:
    print("Images are different")