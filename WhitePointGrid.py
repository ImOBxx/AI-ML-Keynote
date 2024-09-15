import cv2
import dlib
import numpy as np
import random

# Load pre-trained face detector from dlib
detector = dlib.get_frontal_face_detector()

# Load the pre-trained facial landmark predictor
predictor_path = "shape_predictor_68_face_landmarks.dat"  # Ensure this is the correct path
try:
    predictor = dlib.shape_predictor(predictor_path)
except RuntimeError as e:
    print(f"Error loading predictor: {e}")
    exit()

# Start video capture from the default camera (usually the frontal camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture image.")
        break
    
    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = detector(gray)

    if len(faces) == 0:
        print("No faces detected.")

    for face in faces:
        # Predict facial landmarks
        landmarks = predictor(gray, face)
        
        # Convert the landmarks to a numpy array
        landmarks_points = []
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            landmarks_points.append((x, y))
        
        # Draw the triangular grid
        points = np.array(landmarks_points, np.int32)
        convexhull = cv2.convexHull(points)
        cv2.polylines(frame, [convexhull], True, (255, 0, 0), 1)
        
        # Create Delaunay triangulation
        rect = cv2.boundingRect(convexhull)
        subdiv = cv2.Subdiv2D(rect)
        subdiv.insert(landmarks_points)
        triangles = subdiv.getTriangleList()
        triangles = np.array(triangles, dtype=np.int32)
        
        for t in triangles:
            pt1 = (int(t[0]), int(t[1]))
            pt2 = (int(t[2]), int(t[3]))
            pt3 = (int(t[4]), int(t[5]))
            
            # Generate a random color for each triangle
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            
            # Check if the points of the triangle are inside the convex hull
            if cv2.pointPolygonTest(convexhull, pt1, False) >= 0 and \
               cv2.pointPolygonTest(convexhull, pt2, False) >= 0 and \
               cv2.pointPolygonTest(convexhull, pt3, False) >= 0:
                cv2.line(frame, pt1, pt2, color, 1)
                cv2.line(frame, pt2, pt3, color, 1)
                cv2.line(frame, pt3, pt1, color, 1)
                
                # Draw white points at the vertices
                cv2.circle(frame, pt1, 2, (255, 255, 255), -1)
                cv2.circle(frame, pt2, 2, (255, 255, 255), -1)
                cv2.circle(frame, pt3, 2, (255, 255, 255), -1)

    # Display the resulting frame
    cv2.imshow('Face with Multicolored Grid and White Points', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the windows
cap.release()
cv2.destroyAllWindows()
