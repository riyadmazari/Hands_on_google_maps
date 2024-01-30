import cv2

def preprocess_frame(frame, img_size=(64, 64)):
    frame = cv2.resize(frame, img_size)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = frame / 255.0
    frame = frame.reshape(1, img_size[0], img_size[1], 1)
    return frame
