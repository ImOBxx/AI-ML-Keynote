import cv2
import numpy as np

# Function to draw the grid on the detected face
def draw_grid_on_face(image, face):
    (x, y, w, h) = face
    # Define the number of horizontal and vertical lines
    num_horizontal_lines = 5
    num_vertical_lines = 5
    
    # Draw horizontal lines
    for i in range(num_horizontal_lines + 1):
        start_point = (x, y + i * h // num_horizontal_lines)
        end_point = (x + w, y + i * h // num_horizontal_lines)
        cv2.line(image, start_point, end_point, (0, 0, 255), 1)
        
    # Draw vertical lines
    for i in range(num_vertical_lines + 1):
        start_point = (x + i * w // num_vertical_lines, y)
        end_point = (x + i * w // num_vertical_lines, y + h)
        cv2.line(image, start_point, end_point, (0, 0, 255), 1)

# Load pre-trained face detector from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture from the default camera (usually the frontal camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw the grid on each detected face
    for face in faces:
        draw_grid_on_face(frame, face)
    
    # Display the resulting frame
    cv2.imshow('Face with Grid', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the windows
cap.release()
cv2.destroyAllWindows()
