import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io
import base64

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"status": "ready", "message": "Backend di folder backend/ aman!"})

@app.route('/process-image', methods=['POST'])
def process():
    return jsonify({"message": "Berhasil"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
