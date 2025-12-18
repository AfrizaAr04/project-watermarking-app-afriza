import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # <--- PASTIKAN BARIS INI ADA
from PIL import Image
import io
import base64

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return jsonify({"status": "ready", "message": "Backend Fix!"})

# ... sisa route lainnya ...
