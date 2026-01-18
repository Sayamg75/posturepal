import cv2
import mediapipe as mp
import numpy as np
import base64
import time

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# ---------- GLOBAL STATE ----------
BASELINE = None
BASELINE_TIME = None
CALIBRATION_DURATION = 5  # seconds

def analyze_posture(image_base64):
    global BASELINE, BASELINE_TIME

    image_bytes = base64.b64decode(image_base64)
    np_arr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    if image is None:
        return {"status": "error", "tip": "Invalid image"}

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    if not results.pose_landmarks:
        return {"status": "error", "tip": "No body detected"}

    lm = results.pose_landmarks.landmark

    # Key landmarks
    ear = np.array([lm[mp_pose.PoseLandmark.LEFT_EAR].x,
                    lm[mp_pose.PoseLandmark.LEFT_EAR].y])

    shoulder = np.array([lm[mp_pose.PoseLandmark.LEFT_SHOULDER].x,
                         lm[mp_pose.PoseLandmark.LEFT_SHOULDER].y])

    hip = np.array([lm[mp_pose.PoseLandmark.LEFT_HIP].x,
                    lm[mp_pose.PoseLandmark.LEFT_HIP].y])

    # Current posture vector
    posture_vector = ear - shoulder

    now = time.time()

    # ---------- CALIBRATION ----------
    if BASELINE is None:
        if BASELINE_TIME is None:
            BASELINE_TIME = now
            return {
                "status": "calibrating",
                "tip": "Sit upright for 5 seconds to calibrate posture"
            }

        if now - BASELINE_TIME < CALIBRATION_DURATION:
            return {
                "status": "calibrating",
                "tip": "Calibrating... hold good posture"
            }

        BASELINE = posture_vector
        return {
            "status": "good",
            "tip": "Calibration complete. Monitoring posture."
        }

    # ---------- DEVIATION FROM BASELINE ----------
    deviation = np.linalg.norm(posture_vector - BASELINE)

    # VERY SENSITIVE threshold (guaranteed to trigger)
    if deviation > 0.03:
        status = "slouching"
        tip = "Posture deviation detected — straighten up!"
    else:
        status = "good"
        tip = "Good posture"

    return {
        "status": status,
        "tip": tip,
        "deviation": round(float(deviation), 4)
    }
