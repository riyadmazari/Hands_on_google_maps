from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/navigate/<gesture>', methods=['GET'])
def navigate_map(gesture):
    # Define the navigation logic based on the gesture
    navigation_command = ''
    if gesture == 'Up':
        navigation_command = 'pan_up'
    elif gesture == 'Down':
        navigation_command = 'pan_down'
    elif gesture == 'Left':
        navigation_command = 'pan_left'
    elif gesture == 'Right':
        navigation_command = 'pan_right'
    elif gesture == 'In':
        navigation_command = 'zoom_in'
    elif gesture == 'Out':
        navigation_command = 'zoom_out'
    
    # Send the navigation command to the frontend
    return jsonify({'command': navigation_command})

if __name__ == '__main__':
    app.run(debug=True)