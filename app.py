from flask import Flask, jsonify, render_template_string, request
import os
import requests

app = Flask(__name__)

# 首页
@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>HTC Weather Service</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            h1 { color: #333; }
            p { color: #666; }
        </style>
    </head>
    <body>
        <h1>HTC service is running</h1>
        <p>Use <code>/weather?q=Melaka</code> or app URLs to get weather info</p>
    </body>
    </html>
    """)

# 固定城市或 q 参数查询天气
@app.route("/weather")
def weather():
    city = request.args.get("q", "Melaka")
    api_key = os.environ.get("OPENWEATHER_KEY")
    if not api_key:
        return jsonify({"error": "API key not found"})

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    r = requests.get(url)
    return jsonify(r.json())

# 动态定位路由（HTC app %s 替换经纬度）
@app.route("/getweather")
def getweather():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    api_key = os.environ.get("OPENWEATHER_KEY")
    if not api_key:
        return jsonify({"error": "API key not found"})
    if not lat or not lon:
        return jsonify({"error": "Missing lat/lon"})

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    r = requests.get(url)
    return jsonify(r.json())

# 静态城市代码查询（HTC app %ls 替换城市代码）
@app.route("/getstaticweather")
def getstaticweather():
    loc = request.args.get("locCode", "Melaka")
    api_key = os.environ.get("OPENWEATHER_KEY")
    if not api_key:
        return jsonify({"error": "API key not found"})

    url = f"https://api.openweathermap.org/data/2.5/weather?q={loc}&appid={api_key}&units=metric"
    r = requests.get(url)
    return jsonify(r.json())

if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host=HOST, port=PORT)
