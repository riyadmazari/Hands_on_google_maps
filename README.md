# Hand Gesture Recognition for Google Maps Navigation

## Introduction
This project is designed to interpret hand gestures as commands for navigating Google Maps. It utilizes a Convolutional Neural Network (CNN) to recognize hand gestures from a webcam feed.

## Project Structure

    ├── gestures             # Training images for each gesture
    │   ├── Down
    │   ├── In
    │   ├── Left
    │   ├── Out
    │   ├── Right
    │   └── Up
    ├── models               # Saved models and label binarizers
    │   ├── gesture_model.h5
    │   └── label_binarizer.pkl
    ├── templates            # HTML templates for Flask app
    │   └── index.html
    ├── .env                 # Environment variables
    ├── app.py               # Flask app main file
    ├── data_preparation.py  # Script for data preparation
    ├── preprocessing.py     # Script for preprocessing the data
    ├── real_time_prediction.py # Real-time gesture recognition script
    ├── requirements.txt     # Required Python packages
    ├── train_model.py       # Script for model training
    └── README.md            # README file

## Setup Instructions

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Prepare and preprocess the dataset:

```bash
python preprocessing.py
python data_preparation.py
```

3. Train the gesture recognition model:

```bash
python train_model.py
```

4. Try model's predictions:

```bash
python real_time_prediction.py
```

5. Run the app:

```bash
python app.py
```
## Contributing

To contribute to this project, please create a branch and submit a pull request for review.