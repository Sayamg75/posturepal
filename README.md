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
