import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return "HTC Weather Server is running!"

@app.route("/weather")
def weather():
    city = request.args.get("q", "Melaka")  # 默认城市 Melaka
    api_key = os.environ.get("OPENWEATHER_KEY")

    if not api_key:
        return jsonify({"error": "API key not configured"}), 500

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    r = requests.get(url)

    if r.status_code != 200:
        return jsonify({"error": "Failed to fetch weather"}), r.status_code

    data = r.json()
    return jsonify({
        "location": data.get("name", city),
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
