import React, { useEffect, useState } from "react";
import { getChampions } from "../api";

const ChampionsTable = () => {
  const [data, setData] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    getChampions().then(setData);
  }, []);

  const filtered = data.filter((c) =>
    c.CustomerID.toString().includes(search)
  );

  return (
    <>
      <input
        placeholder="Search CustomerID"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        style={{ marginBottom: "10px", padding: "5px" }}
      />

      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>CustomerID</th>
            <th>Recency</th>
            <th>Frequency</th>
            <th>Monetary</th>
            <th>RFM</th>
          </tr>
        </thead>
        <tbody>
          {filtered.map((c) => (
            <tr key={c.CustomerID}>
              <td>{c.CustomerID}</td>
              <td>{c.Recency}</td>
              <td>{c.Frequency}</td>
              <td>{c.Monetary.toFixed(2)}</td>
              <td>{c.RFM_Score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
};

export default ChampionsTable;
