from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# -----------------------------
# PATH FIX (IMPORTANT)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))     # scripts/
PROJECT_DIR = os.path.dirname(BASE_DIR)                   # rfm-project/
DATA_DIR = os.path.join(PROJECT_DIR, "data")

FILE_PATH = os.path.join(DATA_DIR, "rfm_segmented.csv")

print("Loading file from:", FILE_PATH)

rfm = pd.read_csv(FILE_PATH)

# -----------------------------
# ROUTES
# -----------------------------
@app.route("/customers")
def customers():
    return jsonify(rfm.to_dict(orient="records"))

@app.route("/segments")
def segments():
    return jsonify(rfm["Segment"].value_counts().to_dict())

@app.route("/champions")
def champions():
    champions = rfm[rfm["Segment"] == "Champions"]
    return jsonify(champions.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
