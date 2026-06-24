import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned NAV data
df = pd.read_csv("data/processed/nav_history_clean.csv")

print("Rows loaded:", len(df))

# Save into SQLite table
df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded into SQLite successfully!")