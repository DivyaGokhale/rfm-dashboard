import React from "react";
import SegmentCards from "./components/SegmentCards";
import ChampionsTable from "./components/ChampionsTable";
import SegmentChart from "./components/SegmentChart";


function App() {
  return (
    <div style={{ padding: "30px" }}>
      <h1>RFM Customer Dashboard</h1>

      <h2>Customer Segments</h2>
      <SegmentCards />

      <h2 style={{ marginTop: "40px" }}>Champions</h2>
      <ChampionsTable />
      
      <h2 style={{ marginTop: "40px" }}>Customer Segments Chart</h2>
      <SegmentChart />

    </div>
  );
}

export default App;
