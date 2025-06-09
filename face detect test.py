import cv2
import os

# --- Configuration ---
# Path to the Haar Cascade XML file for face detection.
# Make sure 'haarcascade_frontalface_default.xml' is in the same directory as this script,
# or provide the full path to it.
haar_cascade_path = "haarcascade_frontalface_default.xml"

# Directory where the dataset will be stored.
dataset_name = "dataset"

# Subdirectory for the specific person's images.
subject_name = "jim"

# Target dimensions for the resized face images (width, height).
# This ensures all captured face images have a consistent size.
target_width = 130
target_height = 100

# Number of face images to capture for the dataset.
num_images_to_capture = 30

# --- Prepare Dataset Directory ---
# Construct the full path for the subject's dataset folder.
save_path = os.path.join(dataset_name, subject_name)

# Check if the directory exists. If not, create it.
if not os.path.isdir(save_path):
    os.makedirs(save_path)
    print(f"Created directory: {save_path}")
else:
    print(f"Directory already exists: {save_path}")

# --- Load the Haar Cascade Classifier ---
# Attempt to load the pre-trained Haar Cascade XML file for face detection.
cascade_classifier = cv2.CascadeClassifier(haar_cascade_path)

# IMPORTANT: Check if the cascade classifier loaded successfully.
# If the file is not found or is corrupted, cascade_classifier.empty() will return True.
if cascade_classifier.empty():
    print(f"ERROR: Could not load Haar Cascade classifier from '{haar_cascade_path}'.")
    print("Please ensure the 'haarcascade_frontalface_default.xml' file is:")
    print("1. In the same directory as this Python script.")
    print("2. Correctly named.")
    print("3. Not corrupted.")
    exit() # Exit the script if the cascade file cannot be loaded.

# --- Initialize Webcam ---
# Try to open the default webcam (index 0).
# If you have multiple webcams or a different default, you might need to try 1, 2, etc.
webcam = cv2.VideoCapture(0)

# IMPORTANT: Check if the webcam was opened successfully.
# This is the most likely cause of your original warnings.
if not webcam.isOpened():
    print("ERROR: Could not open webcam.")
    print("Possible reasons for webcam access failure:")
    print("1. The webcam is currently in use by another application (e.g., Zoom, Teams, another camera app).")
    print("   Please close all other applications that might be using the camera.")
    print("2. Incorrect webcam index. Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` or `(2)`.")
    print("3. Missing or outdated webcam drivers. Try updating them.")
    print("4. Insufficient permissions for Python to access the camera (check OS privacy settings).")
    print("5. The webcam is physically disconnected or faulty.")
    exit() # Exit the script if the webcam can't be accessed.

print("Webcam opened successfully. Press 'ESC' to exit manually.")
print(f"Capturing {num_images_to_capture} face images for '{subject_name}'...")

# --- Image Capture Loop ---
image_count = 0 # Initialize count for captured images.

try:
    # Loop until the desired number of images are captured.
    # The loop continues as long as 'image_count' is less than 'num_images_to_capture'.
    while image_count < num_images_to_capture:
        # Read a frame from the webcam.
        # 'ret' (return) is a boolean indicating if the frame was successfully read.
        # 'frame' is the actual image frame.
        ret, frame = webcam.read()

        # If frame reading failed (e.g., webcam disconnected), break the loop.
        if not ret:
            print("Failed to grab frame from webcam. Exiting.")
            break

        # Convert the captured frame to grayscale.
        # Face detection algorithms often work better on grayscale images.
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame using the loaded cascade classifier.
        # Arguments:
        #   - image: The grayscale image to search for faces.
        #   - scaleFactor: Parameter specifying how much the image size is reduced at each image scale.
        #                  (e.g., 1.3 means image is scaled down by 30% each time).
        #   - minNeighbors: Parameter specifying how many neighbors each candidate rectangle should have to retain it.
        #                   Higher values result in fewer detections but higher quality.
        faces = cascade_classifier.detectMultiScale(gray_frame, 1.3, 5) # Increased minNeighbors for better stability.

        # Iterate over all detected faces in the current frame.
        for (x, y, w, h) in faces:
            # Draw a green rectangle around the detected face in the original color frame.
            # (x,y) are the top-left coordinates, (x+w, y+h) are bottom-right, (0,255,0) is green BGR color, 2 is thickness.
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Extract the Face Region of Interest (ROI) from the grayscale frame.
            # This slices the image to get only the detected face area.
            face_roi = gray_frame[y:y + h, x:x + w]

            # Resize the extracted face region to the target dimensions (target_width x target_height).
            # This is crucial for creating a consistent dataset for training a face recognition model later.
            resized_face = cv2.resize(face_roi, (target_width, target_height))

            # --- Save the captured and resized face image ---
            # Construct the filename using the current image_count.
            # Using an f-string for clear formatting and os.path.join for platform independence.
            image_filename = os.path.join(save_path, f"{image_count + 1}.png")

            # Save the resized face image to the specified path.
            cv2.imwrite(image_filename, resized_face)
            print(f"Captured {image_count + 1}/{num_images_to_capture} images: {image_filename}")

            # Increment the image_count after successfully saving an image.
            image_count += 1

            # If enough images are captured, break from this inner loop (processing faces in current frame)
            # and the outer loop will also terminate.
            if image_count >= num_images_to_capture:
                break

        # Display the frame with detected faces (and rectangles) in a window.
        cv2.imshow("Face Capture - Press ESC to exit", frame) # Changed window title for clarity.

        # Wait for 10 milliseconds for a key press.
        # '& 0xFF' is used to ensure compatibility across different systems.
        key = cv2.waitKey(10) & 0xFF

        # If the 'ESC' key (ASCII value 27) is pressed, break the loop.
        if key == 27:
            print("ESC key pressed. Exiting capture.")
            break

        # Also break the loop if the desired number of images has been captured.
        if image_count >= num_images_to_capture:
            print(f"Successfully captured {num_images_to_capture} images. Exiting.")
            break

finally:
    # --- Resource Cleanup ---
    # Release the webcam resource. This is very important to free up the camera for other applications.
    webcam.release()
    # Destroy all OpenCV windows that were created.
    cv2.destroyAllWindows()
    print("Webcam and OpenCV windows released. Application closed.")