import pandas as pd
import os


# PATH SETUP
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
FILE_PATH = os.path.join(DATA_DIR, "online_retail.xlsx")

print("Current working directory:", BASE_DIR)
print("Files in data folder:", os.listdir(DATA_DIR))

# LOAD DATA
print("\nLoading Excel dataset...")
df = pd.read_excel(FILE_PATH)

print("Loaded rows:", len(df))
print("Original columns:", df.columns.tolist())

# RENAME COLUMNS (STANDARD)
df = df.rename(columns={
    "Customer ID": "CustomerID",
    "Price": "UnitPrice"
})

# KEEP REQUIRED COLUMNS ONLY
df = df[
    ["CustomerID", "InvoiceDate", "Quantity", "UnitPrice"]
]

# DATA CLEANING
# Remove missing customers
df = df.dropna(subset=["CustomerID"])

# Convert CustomerID to int
df["CustomerID"] = df["CustomerID"].astype(int)

# Remove invalid quantity or price
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["order_value"] = df["Quantity"] * df["UnitPrice"]

print("\nAfter cleaning:")
print("Rows:", len(df))
print(df.head())
print(df.info())

# SAVE OUTPUT
OUTPUT_PATH = os.path.join(DATA_DIR, "cleaned_retail_minimal.csv")
df.to_csv(OUTPUT_PATH, index=False)

print("\nCleaned file saved to:", OUTPUT_PATH)
