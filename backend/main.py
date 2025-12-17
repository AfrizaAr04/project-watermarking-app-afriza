from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Backend di Vercel Aktif!"})

# Tambahkan route lainnya di sini...
