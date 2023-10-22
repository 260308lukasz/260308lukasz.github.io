import os
import requests
from flask import send_from_directory, current_app

def download_weather_icon(app, icon_code):
    url = f"http://openweathermap.org/img/w/{icon_code}.png"
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(os.path.join(app.root_path, 'static/weather_icons'), exist_ok=True)
        with open(os.path.join(app.root_path, f"static/weather_icons/{icon_code}.png"), "wb") as f:
            f.write(response.content)


def serve_custom_static(app):
    @app.route('/static/weather_icons/<path:filename>')
    def custom_static(filename):
        return send_from_directory(app.root_path + '/static/weather_icons', filename)

def get_weather(city):
    api_key = current_app.config['API_KEY']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        
        temperature = weather_data.get('main', {}).get('temp')
        humidity = weather_data.get('main', {}).get('humidity')
        wind_speed = weather_data.get('wind', {}).get('speed')
        description = weather_data.get('weather', [{}])[0].get('description')
        
        result = {
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'description': description,
            'weather': weather_data.get('weather', []),
        }

        return result
    else:
        return None

def get_forecast(city):
    with current_app.app_context():
        api_key = current_app.config['API_KEY']
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            forecast_data = response.json()
            
            return forecast_data
        else:
            return None
