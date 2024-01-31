# Hand Gesture Recognition for Google Maps Navigation

This project implements a hand gesture recognition system to control Google Maps navigation. It uses a Convolutional Neural Network (CNN) to classify hand gestures captured via webcam and translates these gestures into navigation commands.

## Project Structure

The project is organized as follows:

- `Up/`, `Down/`, `Right/`, `Left/`, `In/`, `Out/`: Directories containing the dataset images for each respective gesture.
- `models/`: Directory where the trained model is saved.
- `utils/`: Contains utility scripts for data preparation and image preprocessing.
- `train_model.py`: Script for training the CNN model.
- `real_time_prediction.py`: Script for running the hand gesture recognition in real-time.
- `map_navigation.py`: Placeholder script for integrating with Google Maps API (or simulation).

## Files Description

- `utils/data_preparation.py`: Loads and preprocesses the image data, splits it into training and testing sets.
- `utils/preprocessing.py`: Contains functions to preprocess individual frames captured from the webcam in real-time.
- `train_model.py`: Defines and trains the CNN model, and saves it to the `models/` directory.
- `real_time_prediction.py`: Captures live video from the webcam, processes frames, and uses the trained model to predict gestures.
- `map_navigation.py`: (Placeholder) This script should contain the logic to translate recognized gestures into Google Maps commands.

## How to Run

1. Ensure you have all the required packages installed:
```bash
   pip install -r requirements.txt
```

3. Train the model by running:
```bash
   python train_model.py
```

5. After training, run the real-time prediction script:
```bash
   python real_time_prediction.py
```


## Requirements

Python 3.6+ and the following packages are required:

- numpy
- opencv-python
- scikit-learn
- tensorflow

See `requirements.txt` for versions.

## Contribution

Feel free to contribute to this project by submitting issues or pull requests on your own branch.
