import pyautogui

# Function to simulate map navigation based on the gesture recognized.
def navigate_map(gesture):
    if gesture == 'Up':
        pyautogui.press('up')  # Simulate pressing the up arrow key
        print("Navigating Up")
    elif gesture == 'Down':
        pyautogui.press('down')  # Simulate pressing the down arrow key
        print("Navigating Down")
    elif gesture == 'Left':
        pyautogui.press('left')  # Simulate pressing the left arrow key
        print("Navigating Left")
    elif gesture == 'Right':
        pyautogui.press('right')  # Simulate pressing the right arrow key
        print("Navigating Right")
    elif gesture == 'In':
        pyautogui.scroll(500)  # Simulate scrolling up to zoom in
        print("Zooming In")
    elif gesture == 'Out':
        pyautogui.scroll(-500)  # Simulate scrolling down to zoom out
        print("Zooming Out")
