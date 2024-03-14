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

## File Descriptions

- `requirements.txt`: Lists all the Python dependencies required to run the project. Install these with `pip install -r requirements.txt`.
- `app.py`: The Flask application that serves the web interface for gesture-controlled navigation. It also handles the backend logic to integrate real-time gesture recognition with Google Maps.
- `data_preparation.py`: Processes the images in the `gestures` directory by extracting features and labels, and prepares the data for model training.
- `preprocessing.py`: Contains functions for image preprocessing to prepare input for the model. This includes resizing, normalizing, and potentially augmenting the data.
- `real_time_prediction.py`: Uses the webcam feed to recognize gestures in real time. It loads the trained model, processes video frames, and identifies hand gestures.
- `train_model.py`: Contains the code to define, compile, and train the CNN model. It processes the prepared data and saves the trained model to disk.
- `templates/index.html`: The HTML template for the Flask application that includes the Google Maps interface and JavaScript code to interact with the backend services.

## Setup Instructions

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Configure the application:

Set your Google Maps API key in the .env file:
```bash
GOOGLE_MAPS_API_KEY=your_api_key_here
```

4. Prepare and preprocess the dataset:

```bash
python preprocessing.py
python data_preparation.py
```

4. Train the gesture recognition model:

```bash
python train_model.py
```

5. Try model's predictions:

```bash
python real_time_prediction.py
```

6. Run the app:

```bash
python app.py
```
## Contributing

To contribute to this project, please create a branch and submit a pull request for review.

## License

Make sure to replace placeholder texts like `your_api_key_here` with actual values. Also, ensure you check and adjust the file paths and names to match your project's actual setup. This `README.md` file should be located in the root directory of your project.
