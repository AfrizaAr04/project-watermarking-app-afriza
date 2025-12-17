from flask_cors import CORS

# ... setelah app = Flask(__name__) ...

CORS(app, resources={r"/*": {
    "origins": ["https://project-watermarking-app-afriza.vercel.app"],
    "methods": ["GET", "POST", "OPTIONS"],
    "allow_headers": ["Content-Type"]
}})
