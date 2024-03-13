import cv2
import mediapipe as mp
import numpy as np
import os
from tensorflow.keras.models import load_model
import pickle

mp_hands = mp.solutions.hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

model_path = '/Users/riyadmazari/Desktop/Hands_on_google_maps/models/gesture_model.h5'
label_binarizer_path = '/Users/riyadmazari/Desktop/Hands_on_google_maps/models/label_binarizer.pkl'

model = load_model(model_path)
with open(label_binarizer_path, 'rb') as f:
    lb = pickle.load(f)

def extract_landmarks(frame):
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_hands.process(image_rgb)
    if result.multi_hand_landmarks:
        landmarks = [[lm.x, lm.y, lm.z] for lm in result.multi_hand_landmarks[0].landmark]
        return np.array(landmarks).flatten()
    return np.zeros(21 * 3)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    landmarks = extract_landmarks(frame)
    
    if landmarks.size > 0:
        prediction = model.predict(np.array([landmarks]))
        gesture_name = lb.classes_[np.argmax(prediction)]
        
        cv2.putText(frame, gesture_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Gesture Recognition', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

mp_hands.close()
cap.release()
cv2.destroyAllWindows()
