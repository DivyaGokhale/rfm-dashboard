import React, { useEffect, useState } from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip } from "recharts";
import { getSegments } from "../api";

const SegmentChart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    getSegments().then((segments) => {
      const formatted = Object.entries(segments).map(
        ([name, value]) => ({ name, value })
      );
      setData(formatted);
    });
  }, []);

  return (
    <BarChart width={600} height={300} data={data}>
      <XAxis dataKey="name" />
      <YAxis />
      <Tooltip />
      <Bar dataKey="value" />
    </BarChart>
  );
};

export default SegmentChart;
