import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # <--- PASTIKAN BARIS INI ADA
from PIL import Image
import io
import base64

app = Flask(__name__)

# Sekarang 'CORS' sudah didefinisikan karena diimport di atas
CORS(app, resources={r"/*": {
    "origins": "*",  # Sementara pakai bintang dulu untuk memastikan jalan
    "methods": ["GET", "POST", "OPTIONS"],
    "allow_headers": ["Content-Type", "Authorization"]
}})

@app.route('/')
def home():
    return jsonify({"status": "ready", "message": "Backend Fix!"})

# ... sisa route lainnya ...
