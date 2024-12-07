from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("WEATHER_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=["GET"])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City name is required"}), 400
                           
    #OpenWeahterMap APIを呼び出す
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather data"}), 500
    
    data = response.json()
    return jsonify({
         "city": data["name"],
        "description": data["weather"][0]["description"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    })
    
if __name__ == '__main__':
    app.run(debug=True)