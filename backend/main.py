import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # <--- PASTIKAN BARIS INI ADA
from PIL import Image
import io
import base64

app = Flask(__name__)

# Hapus baris CORS yang lama, ganti dengan ini:
from flask_cors import CORS

CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "expose_headers": ["Content-Type", "Authorization"]
    }
})
@app.route('/process-image', methods=['POST', 'OPTIONS'])
def process():
    if request.method == 'OPTIONS':
        return '', 204
    # Jangan proses gambar dulu, tes koneksi saja
    return jsonify({"message": "Koneksi Tembus!"}), 200
    
@app.route('/')
def home():
    return jsonify({"status": "ready", "message": "Backend Fix!"})

# ... sisa route lainnya ...
