import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/weather")
def weather():
    # 获取 URL 参数 q，默认 Melaka
    city = request.args.get("q", "Melaka")
    
    # 从环境变量读取 OpenWeather API key
    api_key = os.environ.get("OPENWEATHER_KEY")
    print("DEBUG: OPENWEATHER_KEY =", api_key)  # 调试打印 Key

    if not api_key:
        return jsonify({"error": "OPENWEATHER_KEY not set in environment"}), 500

    # 构建请求 URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        r = requests.get(url)
        data = r.json()
        
        # 检查 API 返回是否有错误
        if r.status_code != 200:
            return jsonify({
                "error": "Failed to fetch weather",
                "detail": data,
                "response": r.text
            }), r.status_code
        
        # 返回天气信息
        return jsoni
