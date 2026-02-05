import pandas as pd
from datetime import datetime
from backend.scripts.rfm_analysis import calculate_rfm

def test_rfm_metrics():
    data = pd.DataFrame({
        "CustomerID": [1, 1, 2],
        "InvoiceDate": [
            datetime(2024, 1, 1),
            datetime(2024, 1, 5),
            datetime(2024, 1, 3)
        ],
        "TotalPrice": [100, 200, 300]
    })

    rfm = calculate_rfm(data)

    cust1 = rfm[rfm["CustomerID"] == 1].iloc[0]

    assert cust1["Frequency"] == 2
    assert cust1["Monetary"] == 300
