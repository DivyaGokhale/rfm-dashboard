import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
FILE_PATH = os.path.join(DATA_DIR, "rfm_segmented.csv")

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

df = pd.read_csv(FILE_PATH)

# 🔑 STANDARDIZE COLUMN NAMES
df.columns = df.columns.str.lower()

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"
)

df[[
    "customerid",
    "recency",
    "frequency",
    "monetary",
    "rfm_score",
    "segment"
]].rename(columns={"customerid": "customer_id"}).to_sql(
    name="rfm_analysis",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ RFM analysis stored in MySQL")
