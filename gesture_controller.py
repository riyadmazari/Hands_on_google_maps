import pyautogui

class GestureController:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.prev_hand_position = None

    def calculate_position(self, hand_x, hand_y):
        # Convert hand_x and hand_y to screen coordinates
        current_x = int(hand_x * self.screen_width)
        current_y = int(hand_y * self.screen_height)

        if self.prev_hand_position is None:
            self.prev_hand_position = (current_x, current_y)
        else:
            # Here you could apply any smoothing or adjusting logic you deem necessary
            self.prev_hand_position = (current_x, current_y)

        return self.prev_hand_position

    def move_cursor(self, hand_landmarks):
        # Assuming hand_landmarks is a landmark list with x and y being normalized values.
        # Let's assume you're using the index finger tip for cursor movement, which is landmark 8.
        hand_x = hand_landmarks.landmark[8].x
        hand_y = hand_landmarks.landmark[8].y

        x, y = self.calculate_position(hand_x, hand_y)
        pyautogui.moveTo(x, y, duration=0.1)  # Move cursor to (x,y) on the screen


    def start_drag(self):
        pyautogui.mouseDown()

    def stop_drag(self):
        pyautogui.mouseUp()
        self.dragging = False

    def update_dragging(self, dragging):
        if dragging and not self.dragging:
            self.start_drag()
            self.dragging = True
        elif not dragging and self.dragging:
            self.stop_drag()
