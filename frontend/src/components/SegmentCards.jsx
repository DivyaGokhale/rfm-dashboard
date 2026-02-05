import React, { useEffect, useState } from "react";
import { getSegments } from "../api";

const SegmentCards = () => {
  const [segments, setSegments] = useState({});

  useEffect(() => {
    getSegments().then(setSegments);
  }, []);

  return (
    <div style={{ display: "flex", gap: "20px" }}>
      {Object.entries(segments).map(([segment, count]) => (
        <div key={segment} style={{
          padding: "20px",
          border: "1px solid #ccc",
          borderRadius: "8px",
          minWidth: "150px"
        }}>
          <h3>{segment}</h3>
          <p>{count} customers</p>
        </div>
      ))}
    </div>
  );
};

export default SegmentCards;
