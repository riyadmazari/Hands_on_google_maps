import cv2
import numpy as np
from tensorflow.keras.models import load_model
from preprocessing import preprocess_frame
from data_preparation import prepare_data


# Load your trained model
model = load_model('models/gesture_model.h5')

X_train, X_test, y_train, y_test, lb = prepare_data()

def get_gesture(prediction, classes):
    return classes[np.argmax(prediction)]

gesture_classes = lb.classes_

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        processed_frame = preprocess_frame(frame)
        prediction = model.predict(processed_frame)
        gesture = get_gesture(prediction, gesture_classes)
        cv2.putText(frame, f'Gesture: {gesture}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow('Gesture Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
