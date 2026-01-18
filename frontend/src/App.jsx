import React, { useRef, useState, useEffect, useCallback } from "react";
import Webcam from "react-webcam";

function App() {
  const webcamRef = useRef(null);
  const [result, setResult] = useState(null);

  const capture = useCallback(async () => {
    if (!webcamRef.current) return;

    const imageSrc = webcamRef.current.getScreenshot();
    if (!imageSrc) return;

    const base64Image = imageSrc.split(",")[1];

    try {
      const res = await fetch("http://localhost:5005/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ image: base64Image }),
      });

      const data = await res.json();
      setResult(data);
    } catch (e) {}
  }, []);

  useEffect(() => {
    const id = setInterval(capture, 300);
    return () => clearInterval(id);
  }, [capture]);

  const auraColor =
    result?.status === "slouching"
      ? "rgba(255, 0, 0, 0.8)"
      : result?.status === "calibrating"
      ? "rgba(255, 200, 0, 0.6)"
      : "rgba(0, 255, 150, 0.6)";

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>PosturePal</h1>

      <div
        style={{
          width: "420px",
          margin: "0 auto",
          boxShadow: `0 0 40px 18px ${auraColor}`,
          borderRadius: "12px",
          transition: "box-shadow 0.2s ease",
        }}
      >
        <Webcam
          ref={webcamRef}
          screenshotFormat="image/jpeg"
          width={400}
          height={300}
          videoConstraints={{ facingMode: "user" }}
          style={{ borderRadius: "12px" }}
        />
      </div>

      {result && (
        <div style={{ marginTop: "15px" }}>
          <h3>{result.status.toUpperCase()}</h3>
          <p>{result.tip}</p>
          {result.deviation && (
            <p style={{ fontSize: "12px" }}>
              Deviation: {result.deviation}
            </p>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
