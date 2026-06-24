import pandas as pd
import os

RAW_FILE = "data/raw/all_live_nav_combined.csv"
OUTPUT_FILE = "data/processed/nav_history_clean.csv"

print("=" * 60)
print("NAV HISTORY CLEANING")
print("=" * 60)

df = pd.read_csv(RAW_FILE)

print("Rows loaded:", len(df))
print("Columns:", df.columns.tolist())

# Convert date
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Convert nav
df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

# Sort
df = df.sort_values(["scheme_code", "date"])

# Remove duplicates
before = len(df)
df = df.drop_duplicates(subset=["scheme_code", "date"])
duplicates_removed = before - len(df)

# Fill missing NAV
missing_before = df["nav"].isna().sum()

df["nav"] = (
    df.groupby("scheme_code")["nav"]
    .transform(lambda x: x.ffill())
)

missing_after = df["nav"].isna().sum()

# Remove invalid NAV
before_validation = len(df)
df = df[df["nav"] > 0]
invalid_removed = before_validation - len(df)

os.makedirs("data/processed", exist_ok=True)

df.to_csv(OUTPUT_FILE, index=False)

print("\nDuplicates removed :", duplicates_removed)
print("Missing NAV before :", missing_before)
print("Missing NAV after  :", missing_after)
print("Invalid rows removed:", invalid_removed)
print("Final rows :", len(df))
print("Saved to :", OUTPUT_FILE)