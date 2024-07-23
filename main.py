import cv2
import numpy as np

# Load the Haar Cascade Classifier for face detection from the correct path
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize the camera
cap = cv2.VideoCapture(0)

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        
        # Display the resulting frame
        cv2.imshow('Face Detection', frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Script interrupted by user.")

finally:
    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()
