import React, { useState } from "react";

const segments = [
  "Champions",
  "Loyal Customers",
  "Potential Loyalists",
  "At Risk",
  "Others"
];

const SegmentCards = ({ onSelectSegment }) => {
  const [active, setActive] = useState("Champions");

  const handleClick = (segment) => {
    setActive(segment);
    onSelectSegment && onSelectSegment(segment);
  };

  return (
    <div style={{ display: "flex", gap: "15px", flexWrap: "wrap" }}>
      {segments.map((segment) => (
        <div
          key={segment}
          onClick={() => handleClick(segment)}
          style={{
            padding: "15px 20px",
            borderRadius: "8px",
            cursor: "pointer",
            backgroundColor: active === segment ? "#2563eb" : "#f1f5f9",
            color: active === segment ? "white" : "black",
            fontWeight: "600",
          }}
        >
          {segment}
        </div>
      ))}
    </div>
  );
};

export default SegmentCards;