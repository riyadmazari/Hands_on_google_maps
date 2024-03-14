import cv2
from gesture_recognition import HandGestureRecognition
from gesture_controller import GestureController
import pyautogui

def main():
    cap = cv2.VideoCapture(0)
    gesture_recognizer = HandGestureRecognition()
    screen_width, screen_height = pyautogui.size()
    gesture_controller = GestureController(screen_width, screen_height)

    while True:
        success, img = cap.read()
        if not success:
            break
        img = cv2.flip(img, 1)
        hand_landmarks = gesture_recognizer.detect_hand_gesture(img)
        
        if hand_landmarks:
            gesture_controller.move_cursor(hand_landmarks)
            # Additional control functions can be called here

        cv2.imshow('Hand Tracker', img)
        if cv2.waitKey(5) & 0xFF == 27:  # Press 'ESC' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
