import React, { useState } from "react";
import SegmentCards from "./components/SegmentCards";
import ChampionsTable from "./components/ChampionsTable";
import SegmentChart from "./components/SegmentChart";


function App() {
  const [selectedSegment, setSelectedSegment] = useState("Champions");

  return (
    <div style={{ padding: "30px" }}>
      <h1>RFM Customer Dashboard</h1>

      <h2>Customer Segments</h2>
      <SegmentCards onSelectSegment={setSelectedSegment} />

      <h2 style={{ marginTop: "40px" }}>Customers - {selectedSegment}</h2>
      <ChampionsTable segment={selectedSegment} />
      
      <h2 style={{ marginTop: "40px" }}>Customer Segments Chart</h2>
      <SegmentChart />

    </div>
  );
}

export default App;