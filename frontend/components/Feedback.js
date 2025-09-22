import React from "react";

function Feedback({ feedback }) {
  return (
    <div>
      <p>Status: {feedback.status}</p>
      <p>Tip: {feedback.tip}</p>
    </div>
  );
}

export default Feedback;
