import pandas as pd
import os

def calculate_rfm(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate RFM metrics from transaction data.

    Supported monetary columns:
    - order_value (pipeline)
    - TotalPrice (tests / raw data)
    """

    # ---- Monetary column handling (CRITICAL FIX) ----
    if "order_value" in df.columns:
        monetary_col = "order_value"
    elif "TotalPrice" in df.columns:
        monetary_col = "TotalPrice"
    else:
        raise ValueError("No monetary column found (order_value / TotalPrice)")

    reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    rfm = (
        df.groupby("CustomerID")
        .agg(
            Recency=("InvoiceDate", lambda x: (reference_date - x.max()).days),
            Frequency=("InvoiceDate", "count"),
            Monetary=(monetary_col, "sum")
        )
        .reset_index()
    )

    return rfm

# -------------------- SCRIPT MODE --------------------
if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "..", "data", "cleaned_retail_minimal.csv")

    print("Loading cleaned retail data...")
    df = pd.read_csv(DATA_PATH, parse_dates=["InvoiceDate"])

    print(f"Rows: {len(df)}")
    print(df.head())

    rfm_df = calculate_rfm(df)

    print("\nRFM metrics:")
    print(rfm_df.head())
