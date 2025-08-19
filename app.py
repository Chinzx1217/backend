import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/weather")
def weather():
    city = request.args.get("q", "Melaka")
    
    # 从环境变量读取 OpenWeather API Key
    api_key = os.environ.get("OPENWEATHER_KEY")
    print("DEBUG: OPENWEATHER_KEY =", api_key)  # 调试打印 Key

    if not api_key:
        return jsonify({"error": "OPENWEATHER_KEY not set in environment"}), 500

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        r = requests.get(url)
        data = r.json()
        
        if r.status_code != 200:
            return jsonify({
                "error": "Failed to fetch weather",
                "detail": data,
                "response": r.text
            }), r.status_code

        return jsonify({
            "location": city,
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        })

    except Exception as e:
        return jsonify({
            "error": "Failed to fetch weather",
            "detail": str(e),
            "response": r.text if 'r' in locals() else None
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
