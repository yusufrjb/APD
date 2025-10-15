from flask import Flask, jsonify
import pandas as pd
import os
# cari path relatif berdasarkan lokasi script, bukan working directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "data", "aqi_surabaya.csv")

print("Reading from:", file_path)
df = pd.read_csv(file_path)

app = Flask(__name__)
DATA_PATH = file_path


@app.route("/")
def index():
    return "<h3>Flask API running — access data at /api/data</h3>"


@app.route("/api/data")
def api_data():
    df = pd.read_csv(DATA_PATH)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(df.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(port=5001, debug=True)