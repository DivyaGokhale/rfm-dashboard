import React, { useEffect, useState } from "react";
import { getSegments } from "../api";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const SegmentChart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    getSegments().then((res) => {
      const counts = {};

      res.forEach((c) => {
        counts[c.Segment] = (counts[c.Segment] || 0) + 1;
      });

      const formatted = Object.entries(counts).map(
        ([segment, count]) => ({ segment, count })
      );

      setData(formatted);
    });
  }, []);

  return (
    <div style={{ width: "100%", height: 300 }}>
      <ResponsiveContainer>
        <BarChart data={data}>
          <XAxis dataKey="segment" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="count" fill="#2563eb" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default SegmentChart;
