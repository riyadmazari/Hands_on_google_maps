import os
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
from real_time_prediction import gesture_queue  # Import the queue from your recognition script

load_dotenv()  # This is the function that loads the .env file into the environment variables
app = Flask(__name__)

# Endpoint for the front-end to call to get the latest gesture
@app.route('/get_gesture', methods=['GET'])
def get_gesture():
    if not gesture_queue.empty():
        gesture = gesture_queue.get_nowait()  # Get the gesture without blocking
        return jsonify(gesture=gesture)
    return jsonify(gesture="No gesture")

# Serve the index page
@app.route('/')
def index():
    api_key = os.environ.get('GOOGLE_MAPS_API_KEY')
    return render_template('index.html', api_key=api_key)


if __name__ == '__main__':
    app.run(debug=True)