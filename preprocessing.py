# preprocessing.py
import cv2
import mediapipe as mp
import os



def annotate_and_save_images(input_folder, output_folder, img_size=(64, 64)):
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils 
    
    for gesture in os.listdir(input_folder):
        gesture_path = os.path.join(input_folder, gesture)
        save_path = os.path.join(output_folder, gesture)
        os.makedirs(save_path, exist_ok=True)
        
        for img_file in os.listdir(gesture_path):
            if img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(gesture_path, img_file)
                frame = cv2.imread(img_path)
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = hands.process(frame_rgb)
                
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                save_img_path = os.path.join(save_path, img_file)
                cv2.imwrite(save_img_path, frame)
                
    hands.close()