# backend/app.py
from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from posture import analyze_posture  # posture detection function
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <--- allows frontend requests
socketio = SocketIO(app, cors_allowed_origins="*")

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def home():
    return "PosturePal backend is running!"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    image_base64 = data.get("image")
    if not image_base64:
        return jsonify({"error": "No image provided"}), 400
    result = analyze_posture(image_base64)
    return jsonify(result)

if __name__ == "__main__":
    print("Starting backend server...")
    socketio.run(app, host="0.0.0.0", port=5005, debug=True)


