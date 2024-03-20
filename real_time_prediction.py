import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model
import pickle

# Load the model and label binarizer
model = load_model('models/gesture_model.h5')
with open('models/label_binarizer.pkl', 'rb') as file:
    lb = pickle.load(file)

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def process_and_predict(frame, model, lb):
    # Convert the frame to RGB
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Process the RGB frame to find hand landmarks
    result = mp_hands.process(image_rgb)

    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]

        # Extract the landmarks into a 1D array
        landmarks = np.array([[landmark.x, landmark.y, landmark.z] for landmark in hand_landmarks.landmark]).flatten()
        
        # Reshape to match the model's expected input
        if landmarks.shape[0] == 63:
            landmarks = landmarks.reshape(-1, 63)
            prediction = model.predict(landmarks)
            gesture_name = lb.classes_[np.argmax(prediction)]

            # Draw the hand annotations on the image
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            return gesture_name, frame

    return None, frame

# Main function for recognizing gestures
def recognize_gestures():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue
        
        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)
        
        # Process frame and predict gesture
        gesture, frame_with_landmarks = process_and_predict(frame, model, lb)
        if gesture:
            # Display the detected gesture as text on the frame
            cv2.putText(frame_with_landmarks, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('Real Time Gesture Recognition', frame_with_landmarks)

        # Press 'q' to break the loop
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_gestures()
