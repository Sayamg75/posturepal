from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
from posture import analyze_posture

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def home():
    return "PosturePal backend is running!"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data or "image" not in data:
        return jsonify({"error": "No image provided"}), 400

    try:
        result = analyze_posture(data["image"])
        return jsonify(result)
    except Exception as e:
        print("Backend error:", e)
        return jsonify({
            "status": "error",
            "tip": "Posture analysis failed"
        }), 500

if __name__ == "__main__":
    print("Starting backend on port 5005...")
    socketio.run(app, host="0.0.0.0", port=5005, debug=True)
