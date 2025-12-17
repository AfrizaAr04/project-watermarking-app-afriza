# Di dalam backend/main.py
CORS(app, resources={r"/*": {
    "origins": ["https://project-watermarking-app-afriza.vercel.app"],
    "methods": ["GET", "POST", "OPTIONS"],
    "allow_headers": ["Content-Type", "Authorization"]
}})
