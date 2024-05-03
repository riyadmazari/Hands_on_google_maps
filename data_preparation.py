import cv2
import mediapipe as mp
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
import pickle

mp_hands = mp.solutions.hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5)

def extract_landmarks(image): 
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = mp.hands.process(image_rgb)
    if result.multi_hand_landmarks:
        landmarks = [[lm.x, lm.y, lm.z] for lm in result.multi_hand_landmarks[0].landmark]
        return np.array(landmarks).flatten()
    return np.zeros(21 * 3) # If no hand is detected, return an array of zeros. 

def prepare_data(dataset_dir, model_dir): 
    data = []
    labels = []
    
    for gesture_name in os.listdir(dataset_dir):
        gesture_folder = os.path.join(dataset_dir, gesture_name)
        for img_file in os.listdir(gesture_folder):
            img_path = os.path.join(gesture_folder, img_file)
            image = cv2.imread(img_path)
            if image is not None:
                landmarks = extract_landmarks(image)
                if landmarks.size > 0:
                    data.append(landmarks)
                    labels.append(gesture_name)
    
    mp_hands.close()               
    
    # Convert the data and labels to numpy arrays
    lb = LabelBinarizer()
    labels_encoded = lb.fit_transform(labels)
    X_train, X_test, y_train, y_test = train_test_split(np.array(data), labels_encoded, test_size=0.2, random_state=42)
        
    # Save the label binarizer and the data
    with open(os.path.join(model_dir, 'label_binarizer.pkl'), 'wb') as f:
        pickle.dump(lb, f)
    
    return X_train, X_test, y_train, y_test
 
if __name__ == "__main__": 
    # Define paths
    dataset_dir = 'gestures'
    model_dir = 'models'
    
    # Prepare the data 
    X_train, X_test, y_train, y_test = prepare_data(dataset_dir, model_dir)
    # Save the data for later use 
    np.savez_compressed(os.path.join(model_dir, 'gesture_data.npz'), X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)
  
