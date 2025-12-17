import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io
import base64

app = Flask(__name__)
# Buka akses untuk Vercel
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return jsonify({"status": "ready", "message": "Backend di folder backend aman!"})

@app.route('/process-image', methods=['POST', 'OPTIONS'])
def process():
    return jsonify({"message": "Berhasil terhubung!"})

if __name__ == '__main__':
    # Railway menggunakan port dinamis
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
