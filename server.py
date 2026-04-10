# server.py
from flask import Flask, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder="static")

JSON_FILE = "cpymos_monitor.json"

@app.route("/api/result")
def get_result():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE) as f:
            data = json.load(f)
    else:
        data = {"expression": "", "result": []}
    return jsonify(data)

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    app.run(debug=True)