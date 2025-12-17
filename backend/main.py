import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image, ImageDraw, ImageFont, ImageColor
import io
import base64
import math

# PINDAHKAN KE SINI (Global Scope)
app = Flask(__name__)

# Izinkan CORS agar bisa diakses dari Vercel
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "BACKEND SUDAH FIX!", "status": 200})

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        mode = request.form.get('mode', 'text')
        text = request.form.get('text', 'CONFIDENTIAL')
        
        # Sederhanakan proses untuk tes koneksi
        base_img = Image.open(file.stream).convert("RGBA")
        return jsonify({"status": "Success", "message": f"Gambar {text} diterima"})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Railway akan mencari port secara otomatis
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
