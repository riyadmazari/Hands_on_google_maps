# Hand Gesture Recognition for Google Maps Navigation

## Introduction
This project is designed to interpret hand gestures as commands for navigating Google Maps. It utilizes a Convolutional Neural Network (CNN) to recognize hand gestures from a webcam feed.

## Demo
The demo might take a few seconds to load...

![Demo Video](/demo/demo.gif)

## Project Structure

    ├── gestures            
    │   ├── Down
    │   ├── In
    │   ├── Left
    │   ├── Out
    │   ├── Right
    │   └── Up
    ├── models               
    │   ├── gesture_model.h5
    │   └── label_binarizer.pkl
    ├── templates            
    │   └── index.html
    ├── .env
    ├── app.py
    ├── data_preparation.py
    ├── preprocessing.py
    ├── real_time_prediction.py
    ├── requirements.txt
    ├── train_model.py
    └── README.md            

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

Set your Google Maps API key in the `.env` file:
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
## Methodology

### Model Description for Hand Gesture Recognition

The hand gesture recognition model is a Convolutional Neural Network (CNN) designed to classify images of hand gestures into pre-defined categories. The model is built using TensorFlow and Keras libraries, which are popular for deep learning tasks.

#### Architecture Overview:
Our CNN consists of several layers that process the input images in a hierarchical manner to understand and classify hand gestures:

`Convolutional Layers`: These are the core building blocks of our CNN. They apply a number of filters to the input image to create a feature map. This process captures the local dependencies in the image, such as edges, textures, and patterns associated with different hand gestures.

`Activation Functions`: We use the ReLU (Rectified Linear Unit) activation function in our convolutional layers. ReLU introduces non-linearity to the model, allowing it to learn more complex patterns.

`Pooling Layers`: These layers reduce the spatial dimensions (width and height) of the input volume for the next convolutional layer. It helps in reducing the computational load, memory usage, and also helps with making the detection of features invariant to scale and orientation.

`Flatten Layer`: After several convolutional and pooling layers, the high-level reasoning in the neural network is done via fully connected layers. A flatten layer is used to convert the 2D feature maps into a 1D feature vector.

`Fully Connected (Dense) Layers`: These layers connect every neuron in one layer to every neuron in the next layer. It is in these layers that the classification process occurs, with the final layer outputting the probability distribution over the classes.

`Dropout Layers`: We use dropout regularization to reduce overfitting. During training, this layer will randomly drop out (i.e., set to zero) a number of output features of the layer with a given probability.

`Output Layer`: The last dense layer outputs the probabilities of the input being in each class. We use the softmax activation function in this layer to convert raw scores into probabilities that sum up to one.

#### Training Process:
The model was trained on a dataset consisting of images labeled with the corresponding hand gesture. These images were preprocessed to a uniform size and normalized to have pixel values between 0 and 1. To enhance the model's ability to generalize, we augmented the dataset by applying random transformations like rotations, translations, and flips.

A multi-class cross-entropy loss function was used to quantify how well the model predicted the actual classifications. We used an Adam optimizer for its adaptive learning rate capabilities, which makes it well-suited for deep learning applications.

To prevent overfitting, we monitored the model's performance on a validation set and implemented early stopping in our training process. This halts the training if the validation accuracy does not improve for a set number of epochs.



## Contributing

To contribute to this project, please create a branch and submit a pull request for review.

## Contributors

Our team is composed of four members who have worked collaboratively to make this project successful. Each member has brought their expertise and dedication to various aspects of the project:

- **Ana Sauras**: Focused on the data preparation phase, Ana developed the `preprocessing.py` script, which involved writing functions to preprocess the images to a uniform format for the model. She also created `data_preparation.py`, responsible for loading images from the dataset, extracting features, and preparing the data for training and testing.

- **Riyad Mazari**: As a core developer, Riyad was in charge of the model's backbone. He scripted `train_model.py` to define, train, and validate the convolutional neural network. He also crafted `real_time_prediction.py`, which integrated the trained model to recognize gestures in real-time using the webcam feed. Riyad additionally contributed by capturing a diverse set of hand gesture images to create a comprehensive dataset for training.

- **Cristina Requena and Beatrice Mossberg**: Collaboratively worked on developing the Flask application in `app.py`. They implemented the backend logic to handle HTTP requests and responses, set up the routes for the application, and managed the server-side integration with Google Maps API for the navigation features. Their work ensured that the predictions from the real-time gesture recognition were effectively translated into navigational commands on the map. Cris also took the lead in error handling and debugging, ensuring the application runs smoothly without interruptions, while Bea focused on the front-end integration, scripting the JavaScript to dynamically update Google Maps based on the recognized gestures.

Together, the team's combined efforts have resulted in a functional and interactive application that demonstrates the innovative use of machine learning and web development technologies.

## License

Make sure to replace placeholder texts like `your_api_key_here` with actual values. Also, ensure you check and adjust the file paths and names to match your project's actual setup. This `README.md` file should be located in the root directory of your project.
