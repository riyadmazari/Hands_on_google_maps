import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

def load_images_from_folder(folder, img_size=(64, 64)):
    images = []
    labels = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder, filename)
            img = cv2.imread(img_path)
            if img is not None:
                img = cv2.resize(img, img_size)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = img / 255.0
                images.append(img)
                labels.append(folder.split('/')[-1])
    return images, labels

def prepare_data():
    data = []
    labels = []
    gestures = ['Up', 'Down', 'Right', 'Left', 'In', 'Out']
    for gesture in gestures:
        images, labels_for_gesture = load_images_from_folder(gesture)
        data.extend(images)
        labels.extend(labels_for_gesture)

    data = np.array(data).reshape(-1, 64, 64, 1)
    labels = np.array(labels)

    lb = LabelBinarizer()
    labels = lb.fit_transform(labels)

    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test, lb