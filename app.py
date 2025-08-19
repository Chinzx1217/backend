import requests
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "HTC service is running"

@app.route("/weather")
def weather():
    city = request.args.get("q", "Melaka")
    api_key = os.environ.get("OPENWEATHER_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        r = requests.get(url)
        data = r.json()
        return jsonify({
            "location": city,
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        })
    except Exception as e:
        return jsonify({"error": "Failed to fetch weather", "detail": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
