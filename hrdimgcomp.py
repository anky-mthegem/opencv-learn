import cv2
import numpy as np
 
# Function to capture an image using a connected camera
def capture_image():
    ipcamera = "http://192.168.137.124:8080/video"
    cap = cv2.VideoCapture(0)
    cap.open(ipcamera)  # Use 0 for the default camera
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
    threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
    similarity = 1 - (cv2.countNonZero(threshold) / (image1.shape[0] * image1.shape[1]))
    return similarity * 100
 
# Path to the base image
base_image_path = "captured_image.jpg"
 
# Step 1: Capture a live image from the camera
captured_image = capture_image()
 
# Step 2: Apply Canny edge detection to the captured image
captured_image_edges = canny_edge_detection(captured_image)
 
# Step 3: Load and process the base image with Canny edge detection
base_image = cv2.imread(base_image_path, cv2.IMREAD_GRAYSCALE)
base_image_edges = cv2.Canny(base_image, 100, 200)
#base_image_edges = cv2.imread('canny_image.jpg', 0)
 
# Step 4: Compare the Canny-processed captured image with the base image
similarity_percentage = compare_images(captured_image_edges, base_image_edges)
print(f"Similarity: {similarity_percentage:.2f}%")
 
# Optional: Display the images for visual confirmation
cv2.imshow("Captured Image Edges", captured_image_edges)
cv2.imshow("Base Image Edges", base_image_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
# Threshold for similarity (adjust as needed)
threshold = 90
 
if similarity_percentage >= threshold:
    print("OK Image")
else:
    print("Images are different")