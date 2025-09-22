import React, { useRef, useState, useCallback } from "react";
import Webcam from "react-webcam";

function App() {
  const webcamRef = useRef(null);
  const [result, setResult] = useState(null);

  const capture = useCallback(async () => {
    if (!webcamRef.current) return;
    const screenshot = webcamRef.current.getScreenshot();
    if (!screenshot) return;

    const base64Image = screenshot.split(",")[1];

    try {
      const response = await fetch("http://localhost:5005/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ image: base64Image }),
      });

      const data = await response.json();
      setResult(data);
    } catch (err) {
      console.error("Error contacting backend:", err);
    }
  }, []);

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1> PosturePal</h1>
      <Webcam
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        width={400}
        height={300}
      />
      <div style={{ marginTop: "20px" }}>
        <button onClick={capture}>Analyze Posture</button>
      </div>
      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Status: {result.status}</h3>
          <p>Tip: {result.tip}</p>
        </div>
      )}
    </div>
  );
}

export default App;

