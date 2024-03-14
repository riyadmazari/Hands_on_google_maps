# app.py
from flask import Flask, render_template, jsonify
import multiprocessing
import os

app = Flask(__name__)
gesture_queue = multiprocessing.Queue(maxsize=1)

# Function to run gesture recognition in the background
def run_gesture_recognition(queue):
    import cv2
    import mediapipe as mp
    import numpy as np
    from tensorflow.keras.models import load_model
    import pickle

    # Load model and label binarizer
    model = load_model('models/gesture_model.h5')
    with open('models/label_binarizer.pkl', 'rb') as file:
        lb = pickle.load(file)

    # Set up MediaPipe hands
    mp_hands = mp.solutions.hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # Function to extract landmarks
    def extract_landmarks(frame):
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = mp_hands.process(image_rgb)
        if results.multi_hand_landmarks:
            landmarks = [[lm.x, lm.y, lm.z] for lm in results.multi_hand_landmarks[0].landmark]
            return np.array(landmarks).flatten()
        return None

    # Capture video and recognize gestures
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Unable to access the camera.")
            break
        frame = cv2.flip(frame, 1)
        landmarks = extract_landmarks(frame)
        if landmarks is not None and landmarks.size == 63:
            landmarks = landmarks.reshape(1, 63)
            prediction = model.predict(landmarks)
            gesture_name = lb.classes_[np.argmax(prediction)]
            # Put the most recent gesture in the queue
            if not queue.full():
                if not queue.empty():
                    queue.get_nowait()
                queue.put(gesture_name)
    cap.release()

@app.route('/get_gesture', methods=['GET'])
def get_gesture():
    if not gesture_queue.empty():
        gesture = gesture_queue.get_nowait()
        return jsonify({'gesture': gesture})
    else:
        return jsonify({'gesture': 'No gesture'})

@app.route('/')
def index():
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    return render_template('index.html', api_key=api_key)

# Run Flask app and gesture recognition in separate processes
if __name__ == '__main__':
    p = multiprocessing.Process(target=run_gesture_recognition, args=(gesture_queue,))
    p.start()
    app.run(debug=True, host='0.0.0.0', port=5001)
    p.terminate()
