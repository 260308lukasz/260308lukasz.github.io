#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys
import os
from flask import Flask, render_template, request, current_app
from pathlib import Path
from utils.weather import get_forecast, download_weather_icon, get_weather, get_forecast
from flask import send_from_directory

app = Flask(__name__)
app.config.from_pyfile('config.py')

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miedzymordzie.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

@app.route('/static/weather_icons/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.root_path + '/static/weather_icons', filename)

@app.template_filter('file_exist')
def file_exist(file_path):
    return Path(file_path).is_file()

def generate_footer():
    return render_template('footer.html')

@app.route('/')
def home():
    return render_template('index.html', footer=generate_footer())

@app.route('/browse_interfaces', methods=['GET', 'POST'])
def browse_interfaces():
    icon_path = None
    theme = request.args.get('theme', 'light')
    detail = request.args.get('detail', 'basic')
    display_format_option_value = request.args.get('display_format_option_value', 'text')

    if request.method == 'POST':
        theme = request.form.get('theme', 'light')
        detail = request.form.get('detail', 'basic')
        display_format_option_value = request.form.get('display_format_option_value', 'text')

    city = "Wroclaw"
    weather_data = get_weather(city)

    # Pobierz ikonę i zapisz ją lokalnie
    if weather_data.get('weather'):
        weather_icon = weather_data['weather'][0]['icon']
        print(f"Downloading weather Icon: {weather_icon}")
        download_weather_icon(current_app, weather_icon)
        icon_path = f"/static/weather_icons/{weather_icon}.png"

    print(f"display_format_option_value inside browse_interfaces: {display_format_option_value}")

    print(f"Icon path inside browse_interfaces: {icon_path}")
          
    forecast_data = get_forecast(city)

    print("Forecast Data Type:", type(forecast_data))

    if forecast_data:
        print("Processing forecast:", forecast_data.get('dt_txt', 'Unknown'))

    return render_template(
        'browse_interfaces.html',
        theme=theme,
        detail=detail,
        display_format_option_value=display_format_option_value,
        weather_data=weather_data,
        icon_path=icon_path,
        forecast_data=forecast_data,
        footer=generate_footer()
    )

def file_exists_case_sensitive(file_path):
    return os.path.exists(file_path)

app.jinja_env.filters['file_exists_case_sensitive'] = file_exists_case_sensitive


@app.route('/survey')
def survey():
    return render_template('survey.html', footer=generate_footer())

if __name__ == '__main__':
    main()
