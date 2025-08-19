import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return "HTC Weather Server is running!"

@app.route("/weather")
def weather():
    city = request.args.get("q", "Unknown")
    # 这里你可以以后换成真实天气 API
    return jsonify({
        "location": city,
        "temperature": 25,
        "condition": "Cloudy"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
