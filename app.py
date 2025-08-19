from flask import Flask, jsonify, render_template_string, request
import os
import requests

app = Flask(__name__)

# 首页路由，显示 HTC 服务运行提示
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
        <p>Use <code>/weather?q=Melaka</code> to get weather info</p>
    </body>
    </html>
    """)

# 天气 API 路由
@app.route("/weather")
def weather():
    city = request.args.get("q", "Melaka")
    api_key = os.environ.get("OPENWEATHER_KEY")
    if not api_key:
        return jsonify({"error": "API key not found"
