# backend/posture.py
import cv2    # OpenCV, handles image processing
import mediapipe as mp  # MediaPipe, detects human pose keypoints
import numpy as np  # used for vector math
import base64

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)

def analyze_posture(image_base64):
    """
    image_base64: string from frontend (captured webcam frame)
    returns: dictionary like {'status': 'good', 'tip': 'keep your back straight'}
    """
    # Convert base64 to numpy array (OpenCV image)
    nparr = np.frombuffer(base64.b64decode(image_base64), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert BGR to RGB for Mediapipe
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the image with MediaPipe
    results = pose.process(img_rgb)

    if results.pose_landmarks:
        shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
        hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
        angle = np.arctan2(shoulder.y - hip.y, shoulder.x - hip.x) * 180 / np.pi

        if angle > 160:
            return {"status": "good", "tip": "Great posture!"}
        else:
            return {"status": "slouching", "tip": "Sit up straight!"}
    else:
        return {"status": "unknown", "tip": "No person detected"}
