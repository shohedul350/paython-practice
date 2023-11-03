import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('your_sign_language_model.h5')

# OpenCV setup for webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Preprocess the frame
    # (perform the same preprocessing steps you used during training)

    # Make predictions
    prediction = model.predict(np.expand_dims(frame, axis=0))

    # Get the predicted class
    predicted_class = np.argmax(prediction)

    # Display the result on the frame
    cv2.putText(frame, f'Predicted: {predicted_class}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow('Sign Language Detection', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
