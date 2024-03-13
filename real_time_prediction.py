import cv2
import mediapipe as mp
import numpy as np
import os
from tensorflow.keras.models import load_model
import pickle

# Initialize MediaPipe hands.
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Load the model and the label binarizer.
model = load_model('/Users/riyadmazari/Desktop/Hands_on_google_maps/models/gesture_model.h5')
with open('/Users/riyadmazari/Desktop/Hands_on_google_maps/models/label_binarizer.pkl', 'rb') as f:
    lb = pickle.load(f)

# Function to extract landmarks.
def extract_landmarks(frame, hands):
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(image_rgb)
    if result.multi_hand_landmarks:
        landmarks = [[lm.x, lm.y, lm.z] for lm in result.multi_hand_landmarks[0].landmark]
        return np.array(landmarks).flatten(), result.multi_hand_landmarks[0]
    return np.zeros(21 * 3), None

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip the frame horizontally for a selfie-view display.
    landmarks, hand_landmarks = extract_landmarks(frame, hands)
    
    # Draw the hand annotations on the video.
    if hand_landmarks:
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    if landmarks.size > 0 and not np.all((landmarks == 0)):
        prediction = model.predict(np.array([landmarks]))
        gesture_name = lb.classes_[np.argmax(prediction)]
        cv2.putText(frame, gesture_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    else:
        cv2.putText(frame, 'No hand detected', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('Gesture Recognition', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

hands.close()
cap.release()
cv2.destroyAllWindows()
