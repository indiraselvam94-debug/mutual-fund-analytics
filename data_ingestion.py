"""
data_ingestion.py
=================
Bluestock Fintech – Mutual Fund Analytics Platform
Day 1: Load all 10 CSV datasets, inspect structure, and run basic validation.

CSV files expected in:  data/raw/
Output (processed):     data/processed/
"""

import os
import pandas as pd

# ── Configuration ─────────────────────────────────────────────────────────────

RAW_DIR       = os.path.join("data", "raw")
PROCESSED_DIR = os.path.join("data", "processed")

# Map: friendly name → expected CSV filename inside data/raw/
CSV_FILES = {
    "fund_master"        : "01_fund_master.csv",
    "nav_history"        : "02_nav_history.csv",
    "aum_by_fund_house"  : "03_aum_by_fund_house.csv",
    "monthly_sip"        : "04_monthly_sip.csv",
    "category_inflows"   : "05_category_inflows.csv",
    "folio_count"        : "06_folio_count.csv",
    "scheme_performance" : "07_scheme_performance.csv",
    "transactions"       : "08_transactions.csv",
    "holdings"           : "09_holdings.csv",
    "benchmark"          : "10_benchmark.csv",
}

SEPARATOR = "=" * 65


# ── Helper functions ──────────────────────────────────────────────────────────

def load_csv(name: str, filename: str) -> pd.DataFrame | None:
    """Load a single CSV file and return a DataFrame (or None on failure)."""
    filepath = os.path.join(RAW_DIR, filename)

    if not os.path.exists(filepath):
        print(f"  ⚠️  File not found – skipping: {filepath}")
        return None

    df = pd.read_csv(filepath, low_memory=False)
    return df


def inspect_dataframe(name: str, df: pd.DataFrame) -> None:
    """Print shape, dtypes, head, and missing-value summary for a DataFrame."""
    print(f"\n{'─' * 65}")
    print(f"  📄  Dataset : {name.upper()}")
    print(f"{'─' * 65}")

    # Shape
    print(f"\n  Shape   : {df.shape[0]:,} rows  ×  {df.shape[1]} columns")

    # Column dtypes
    print(f"\n  Column data types:")
    for col, dtype in df.dtypes.items():
        missing = df[col].isna().sum()
        pct     = missing / len(df) * 100
        flag    = "  ⚠️  has nulls" if missing > 0 else ""
        print(f"    • {col:<35} {str(dtype):<12} "
              f"nulls={missing:>6,} ({pct:5.1f}%){flag}")

    # First 3 rows
    print(f"\n  Head (first 3 rows):")
    print(df.head(3).to_string(index=False))

    # Anomaly hints
    anomalies = []
    if df.duplicated().sum() > 0:
        anomalies.append(f"Duplicate rows: {df.duplicated().sum():,}")
    null_cols = df.columns[df.isna().any()].tolist()
    if null_cols:
        anomalies.append(f"Columns with nulls: {null_cols}")

    if anomalies:
        print(f"\n  ⚠️  Anomalies detected:")
        for a in anomalies:
            print(f"    – {a}")
    else:
        print(f"\n  ✅  No obvious anomalies detected.")


def save_processed(name: str, df: pd.DataFrame) -> None:
    """Save a lightly cleaned copy to data/processed/."""
    out_path = os.path.join(PROCESSED_DIR, f"{name}_processed.csv")
    df.to_csv(out_path, index=False)
    print(f"\n  💾  Saved processed file → {out_path}")


def validate_amfi_codes(datasets: dict) -> None:
    """
    Cross-check: every AMFI scheme code in fund_master
    must exist in nav_history.
    """
    print(f"\n{SEPARATOR}")
    print("  🔍  AMFI CODE VALIDATION")
    print(SEPARATOR)

    fm = datasets.get("fund_master")
    nh = datasets.get("nav_history")

    if fm is None or nh is None:
        print("  ⚠️  fund_master or nav_history not loaded – skipping validation.")
        return

    # Try common column names for the scheme code
    fm_code_col = next((c for c in fm.columns if "code" in c.lower()), None)
    nh_code_col = next((c for c in nh.columns if "code" in c.lower()), None)

    if not fm_code_col or not nh_code_col:
        print("  ⚠️  Could not detect scheme-code columns automatically.")
        print(f"     fund_master columns : {list(fm.columns)}")
        print(f"     nav_history columns : {list(nh.columns)}")
        return

    master_codes = set(fm[fm_code_col].dropna().astype(str))
    nav_codes    = set(nh[nh_code_col].dropna().astype(str))

    missing = master_codes - nav_codes
    extra   = nav_codes - master_codes

    print(f"\n  Scheme codes in fund_master : {len(master_codes):,}")
    print(f"  Scheme codes in nav_history  : {len(nav_codes):,}")
    print(f"  Codes in master but NOT nav  : {len(missing):,}")
    print(f"  Codes in nav but NOT master  : {len(extra):,}")

    if not missing:
        print("\n  ✅  All fund_master codes are present in nav_history!")
    else:
        print(f"\n  ⚠️  Missing codes (first 10): {list(missing)[:10]}")


def explore_fund_master(df: pd.DataFrame) -> None:
    """Print unique fund houses, categories, sub-categories, risk grades."""
    print(f"\n{SEPARATOR}")
    print("  🏦  FUND MASTER EXPLORATION")
    print(SEPARATOR)

    for col_hint, label in [
        ("fund_house",    "Fund Houses"),
        ("category",      "Categories"),
        ("sub_category",  "Sub-Categories"),
        ("sub-category",  "Sub-Categories"),
        ("risk",          "Risk Grades"),
    ]:
        col = next((c for c in df.columns if col_hint in c.lower()), None)
        if col:
            uniq = df[col].dropna().unique()
            print(f"\n  {label} ({len(uniq)} unique):")
            for v in sorted(uniq):
                print(f"    • {v}")


# ── Main pipeline ─────────────────────────────────────────────────────────────

def main():
    print(f"\n{SEPARATOR}")
    print("  🚀  MUTUAL FUND ANALYTICS – DATA INGESTION")
    print(f"{SEPARATOR}\n")

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    datasets = {}
    loaded   = []
    skipped  = []

    # ── Step 1: Load all CSVs ─────────────────────────────────────────────────
    print("STEP 1 – Loading CSV files from data/raw/")
    print(SEPARATOR)

    for name, filename in CSV_FILES.items():
        print(f"\n  Loading [{name}] from '{filename}' …")
        df = load_csv(name, filename)
        if df is not None:
            datasets[name] = df
            loaded.append(name)
            print(f"  ✅  Loaded  →  {df.shape[0]:,} rows × {df.shape[1]} cols")
        else:
            skipped.append(name)

    print(f"\n{'─'*65}")
    print(f"  Summary: {len(loaded)} loaded, {len(skipped)} skipped")
    if skipped:
        print(f"  Skipped: {skipped}")

    # ── Step 2: Inspect each loaded dataset ───────────────────────────────────
    if datasets:
        print(f"\n\n{SEPARATOR}")
        print("STEP 2 – Inspecting each dataset (.shape / .dtypes / .head)")
        print(SEPARATOR)

        for name, df in datasets.items():
            inspect_dataframe(name, df)
            save_processed(name, df)

    # ── Step 3: Explore fund_master ───────────────────────────────────────────
    if "fund_master" in datasets:
        explore_fund_master(datasets["fund_master"])

    # ── Step 4: Validate AMFI codes ───────────────────────────────────────────
    validate_amfi_codes(datasets)

    # ── Done ──────────────────────────────────────────────────────────────────
    print(f"\n{SEPARATOR}")
    print("  ✅  Day 1 – Data Ingestion complete!")
    print(f"      Processed files saved to: {PROCESSED_DIR}/")
    print(SEPARATOR)


if __name__ == "__main__":
    main()
