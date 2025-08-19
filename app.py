import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# 根路径，显示服务运行状态
@app.route("/")
def home():
    return "HTC service is running"

# 获取天气信息
@app.route("/weather")
def weather():
    city = request.args.get("q", "Melaka")
    api_key = os.environ.get("OPENWEATHER_KEY")  # 确保 Render 上有设置这个环境变量
    if not api_key:
        return jsonify({"error": "API key not found"})
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        return jsonify({
            "location": city,
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        })
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch weather", "detail": str(e)})

# Render 自动使用 PORT 环境变量
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
