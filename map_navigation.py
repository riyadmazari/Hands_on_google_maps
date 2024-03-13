import requests 
import os 
from dotenv import load_dotenv

load_dotenv()

def get_coordinates(location): 
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"  
    params = {"address": location, "key":api_key}
    response = requests.get(base_url, params=params)
    if response.status_code == 200: 
        latitude = response.json()["results"][0]["geometry"]["location"]["lat"]
        longitude = response.json()["results"][0]["geometry"]["location"]["lng"]
        return latitude, longitude
    else: 
        return None, None 


def navigate_map(api_key, gesture, location): 
    latitude, longitude, zoom = get_coordinates(api_key, location)
    if latitude and longitude: 
        if gesture == 'Up':
            latitude += 0.001
            print("Navigating Up")
        # Add actual navigation logic or API calls
        elif gesture == 'Down':
            latitude -= 0.001
            print("Navigating Down")
        elif gesture == 'Left':
            longitude -= 0.001
            print("Navigating Left")
        elif gesture == 'Right':
            longitude += 0.001
            print("Navigating Right")
        elif gesture == 'In':
            zoom += 1  
            print("Zooming In")
        elif gesture == 'Out':
            zoom -= 1  
            print("Zooming Out")
    else: 
        print("Unable to get coordinates")
        

