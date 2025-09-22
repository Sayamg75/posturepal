import React, { useRef, useEffect } from "react";
import Webcam from "react-webcam";

function WebcamFeed({ socket }) {
  const webcamRef = useRef(null);

  useEffect(() => {
    const interval = setInterval(() => {
      if (webcamRef.current) {
        // capture the current frame as a base64 image
        const imageSrc = webcamRef.current.getScreenshot();
        if (imageSrc) {
          // send it to backend via socket
          socket.emit("frame", { image: imageSrc.split(",")[1] }); 
          // split to remove the "data:image/jpeg;base64," prefix
        }
      }
    }, 1000); // every 1 second

    return () => clearInterval(interval);
  }, [socket]);

  return (
    <div>
      <Webcam
        audio={false}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        width={320}
        height={240}
      />
    </div>
  );
}

export default WebcamFeed;
