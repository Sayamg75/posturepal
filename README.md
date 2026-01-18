### PosturePal

An AI-powered, full-stack posture tracking application that uses real-time computer vision to analyze webcam input and provide live feedback on user posture.

PosturePal helps users improve ergonomics, reduce slouching, and track posture trends over time.


### Tech Stack

**Backend:** Python, Flask, OpenCV, MediaPipe, NumPy  

**Frontend:** React (Vite), React Webcam  


### Key Features

- Real-time posture detection using OpenCV + MediaPipe keypoint estimation  
- Posture classification via shoulder and hip angle analysis (~85–90% accuracy)  
- Live posture alerts and corrective notifications (~95% trigger accuracy)  
- AI-assisted posture tips and longitudinal posture history tracking  


### How It Works

1. Webcam frames are captured in real time through the React frontend  
2. Frames are processed on the Flask backend using OpenCV and MediaPipe  
3. Key body landmarks are extracted and evaluated using angle-based heuristics  
4. Feedback and alerts are returned to the frontend in real time  
5. Posture data is summarized to provide historical insights

## Frontend

To run the frontend, execute the following commands from the project root:
cd frontend
npm install
npm run dev

The frontend will run locally at:

http://localhost:5173


---

## Backend

To run the backend, execute the following commands from the project root:
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py


The backend server will run locally at:

http://localhost:5005


---

## Usage

With both the backend and frontend running, open the frontend URL in a browser and allow webcam access. On first launch, the application performs a short calibration period during which the user should sit upright. After calibration, posture is monitored continuously in real time.

A green visual aura indicates good posture, while a red aura signals that poor posture has been detected and corrective action is recommended.

---

## Notes

For best results, ensure that the user’s upper body and shoulders are clearly visible to the camera and that the environment is well lit. Calibration is required once per session to maintain accurate posture detection.

---






