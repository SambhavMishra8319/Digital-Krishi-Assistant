import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#from config import OPENWEATHER_API_KEY
OPENWEATHER_API_KEY = "aef77b9d116022a2de93209182565667"

def get_weather(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        rain = data.get('rain', {}).get('1h', 0.0)  # rainfall in mm last hour, 0 if none
        return temp, humidity, rain
    else:
        raise Exception(f"Weather API error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    print(get_weather("Pune"))  # Test fetch, can be removed if you want
