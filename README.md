# Hand Gesture Recognition for Cursor Movement

## Overview

The Hand Gesture Recognition for Cursor Movement, is designed to offer an intuitive method for moving the cursor over a window. By leveraging hand gesture recognition through a webcam, users can interact with interfaces in a seamless and natural manner. This document outlines the system's architecture, installation process, and operational guidelines.

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.6 or newer
- **Dependencies**: OpenCV, MediaPipe, PyAutoGUI

## Installation

Ensure Python 3.6 or newer is installed on your system. Install the project dependencies by executing the following command in your terminal:

```bash
pip install opencv-python mediapipe pyautogui
``````
## File Structure
- `main.py` - Initiates the application and integrates all components.
- `gesture_recognition.py` - Handles the detection of hand gestures using MediaPipe.
- `gesture_controller.py` - Translates recognized hand gestures into map navigation commands.
- `requirements.txt` - Lists all Python dependencies for the project.
## Usage
1. **Start the Application**: Run main.py to initiate the gesture-controlled map navigation system.

```bash
python main.py
``````
2. **Navigate**: Utilize the predefined gestures to interact with the interface. Currently the following gestures are supported:

   - **Move Cursor**: Navigate by the cursor following the user's index finger.

## Development
- **Gesture Recognition Module** (gesture_recognition.py): Implements real-time hand tracking and gesture detection leveraging the MediaPipe library.
- **Gesture Controller Module** (gesture_controller.py): Interprets detected gestures and translates them into map navigation actions using PyAutoGUI.
## Contributing
Contributions to the Gesture-Controlled Map Navigation System are welcome. To contribute, please fork the repository, make your changes, and submit a pull request with a comprehensive description of your updates.