import React, { useEffect, useState } from "react";
import { getCustomers } from "../api";

const ROWS_PER_PAGE = 10;

const ChampionsTable = ({ segment = "Champions" }) => {
  const [data, setData] = useState([]);
  const [search, setSearch] = useState("");
  const [page, setPage] = useState(1);

  useEffect(() => {
    setPage(1);

    // Get all customers and filter by segment
    getCustomers().then((res) => {
      const filtered = res.filter(
        (c) => c.Segment === segment
      );
      setData(filtered);
    });
  }, [segment]);

  const searched = data.filter((c) =>
    c.CustomerID.toString().includes(search)
  );

  const start = (page - 1) * ROWS_PER_PAGE;
  const end = start + ROWS_PER_PAGE;
  const pageData = searched.slice(start, end);

  return (
    <>
      <input
        placeholder="Search CustomerID"
        value={search}
        onChange={(e) => {
          setSearch(e.target.value);
          setPage(1);
        }}
        style={{ marginBottom: "10px" }}
      />

      <div style={{ maxHeight: "350px", overflowY: "auto" }}>
        <table border="1" width="100%">
          <thead>
            <tr>
              <th>CustomerID</th>
              <th>Recency</th>
              <th>Frequency</th>
              <th>Monetary</th>
              <th>RFM_Score</th>
            </tr>
          </thead>
          <tbody>
            {pageData.map((c) => (
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
      </div>

      {/* Pagination */}
      <div style={{ marginTop: "10px" }}>
        <button
          disabled={page === 1}
          onClick={() => setPage((p) => p - 1)}
        >
          Prev
        </button>

        <span style={{ margin: "0 10px" }}>
          Page {page} of {Math.ceil(searched.length / ROWS_PER_PAGE)}
        </span>

        <button
          disabled={end >= searched.length}
          onClick={() => setPage((p) => p + 1)}
        >
          Next
        </button>
      </div>
    </>
  );
};

export default ChampionsTable;