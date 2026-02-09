import pandas as pd
import os

def calculate_rfm(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate RFM metrics, scores, and segments.
    """

    # Monetary column handling
    if "order_value" in df.columns:
        monetary_col = "order_value"
    elif "TotalPrice" in df.columns:
        monetary_col = "TotalPrice"
    else:
        raise ValueError("No monetary column found (order_value / TotalPrice)")

    # Reference date
    reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    # RFM Metrics
    rfm = (
        df.groupby("CustomerID")
        .agg(
            Recency=("InvoiceDate", lambda x: (reference_date - x.max()).days),
            Frequency=("InvoiceNo", "nunique"),   # ✅ FIXED
            Monetary=(monetary_col, "sum")
        )
        .reset_index()
    )

    # Data Quality Filters
    rfm = rfm[
        (rfm["Recency"] >= 0) &
        (rfm["Frequency"] >= 1) &
        (rfm["Monetary"] > 0)
    ]

    # RFM Scoring (Quantiles)
    rfm["R_Score"] = pd.qcut(
        rfm["Recency"], 5, labels=[5, 4, 3, 2, 1]
    ).astype(int)

    rfm["F_Score"] = pd.qcut(
        rfm["Frequency"], 5, labels=[1, 2, 3, 4, 5]
    ).astype(int)

    rfm["M_Score"] = pd.qcut(
        rfm["Monetary"], 5, labels=[1, 2, 3, 4, 5]
    ).astype(int)

    # RFM Score & Code
    rfm["RFM_Score"] = rfm["R_Score"] + rfm["F_Score"] + rfm["M_Score"]
    rfm["RFM_Code"] = (
        rfm["R_Score"].astype(str) +
        rfm["F_Score"].astype(str) +
        rfm["M_Score"].astype(str)
    )

    # Customer Segmentation
    def segment(row):
        if row["RFM_Code"] == "555":
            return "Champions"
        elif row["R_Score"] >= 4 and row["F_Score"] >= 4:
            return "Loyal Customers"
        elif row["R_Score"] >= 4:
            return "Potential Loyalists"
        elif row["R_Score"] <= 2 and row["F_Score"] >= 3:
            return "At Risk"
        else:
            return "Lost Customers"

    rfm["Segment"] = rfm.apply(segment, axis=1)

    return rfm


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "..", "data", "cleaned_retail_minimal.csv")
    OUTPUT_DIR = os.path.join(BASE_DIR, "..", "outputs")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Loading cleaned retail data...")
    df = pd.read_csv(DATA_PATH, parse_dates=["InvoiceDate"])

    print(f"Rows loaded: {len(df)}")

    rfm_df = calculate_rfm(df)

    # Segment Summary
    segment_summary = rfm_df.groupby("Segment").agg(
        customer_count=("CustomerID", "count"),
        avg_recency=("Recency", "mean"),
        avg_frequency=("Frequency", "mean"),
        avg_monetary=("Monetary", "mean"),
        total_revenue=("Monetary", "sum")
    ).round(2).reset_index()

    # Save Outputs
    rfm_df.to_csv(os.path.join(OUTPUT_DIR, "rfm_table.csv"), index=False)
    segment_summary.to_csv(os.path.join(OUTPUT_DIR, "segment_summary.csv"), index=False)

    print("📁 Outputs:")
    print("- rfm_table.csv")
    print("- segment_summary.csv")
