"""
live_nav_fetch.py
=================
Bluestock Fintech – Mutual Fund Analytics Platform
Day 1: Fetch live NAV data from mfapi.in for 5 key schemes.

API base : https://api.mfapi.in/mf/{scheme_code}
Output   : data/raw/live_nav_{scheme_code}.csv
           data/raw/all_live_nav_combined.csv
"""

import os
import time
import requests
import pandas as pd
from datetime import datetime

# ── Configuration ─────────────────────────────────────────────────────────────

API_BASE = "https://api.mfapi.in/mf"
RAW_DIR  = os.path.join("data", "raw")

SCHEMES = {
    "HDFC Top 100 Direct"        : 125497,
    "SBI Bluechip Direct"        : 119551,
    "ICICI Pru Bluechip Direct"  : 120503,
    "Nippon Large Cap Direct"    : 118632,
    "Axis Bluechip Direct"       : 119092,
    "Kotak Bluechip Direct"      : 120841,
}

SEPARATOR = "=" * 65


# ── Fetch function ────────────────────────────────────────────────────────────

def fetch_nav(scheme_name: str, scheme_code: int) -> pd.DataFrame | None:
    """
    Call mfapi.in for a single scheme code.
    Returns a cleaned DataFrame with columns:
        scheme_code, scheme_name, date, nav
    """
    url = f"{API_BASE}/{scheme_code}"
    print(f"\n  🌐  GET {url}")

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()          # raises if HTTP error
        data = response.json()
    except requests.exceptions.ConnectionError:
        print(f"  ❌  Network error – check your internet connection.")
        return None
    except requests.exceptions.Timeout:
        print(f"  ❌  Request timed out after 15 seconds.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"  ❌  HTTP error: {e}")
        return None
    except ValueError:
        print(f"  ❌  Could not parse JSON response.")
        return None

    # ── Parse JSON structure ──────────────────────────────────────────────────
    # mfapi.in returns:
    # {
    #   "meta": { "scheme_code": ..., "scheme_name": ..., ... },
    #   "data": [ {"date": "DD-MM-YYYY", "nav": "123.456"}, ... ]
    # }

    meta      = data.get("meta", {})
    nav_data  = data.get("data", [])

    if not nav_data:
        print(f"  ⚠️  No NAV data returned for scheme {scheme_code}.")
        return None

    df = pd.DataFrame(nav_data)                        # columns: date, nav

    # Clean & type-cast
    df["nav"]         = pd.to_numeric(df["nav"], errors="coerce")
    df["date"]        = pd.to_datetime(df["date"], format="%d-%m-%Y", errors="coerce")
    df["scheme_code"] = scheme_code
    df["scheme_name"] = scheme_name
    df["fund_house"]  = meta.get("fund_house", "")
    df["scheme_type"] = meta.get("scheme_type", "")
    df["scheme_category"] = meta.get("scheme_category", "")

    # Sort chronologically
    df = df.sort_values("date").reset_index(drop=True)

    # Reorder columns
    df = df[["scheme_code", "scheme_name", "fund_house",
             "scheme_type", "scheme_category", "date", "nav"]]

    print(f"  ✅  Fetched {len(df):,} NAV records")
    print(f"      Date range : {df['date'].min().date()} → {df['date'].max().date()}")
    print(f"      Latest NAV : ₹{df['nav'].iloc[-1]:,.4f}  ({df['date'].iloc[-1].date()})")

    return df


def save_individual(df: pd.DataFrame, scheme_code: int, scheme_name: str) -> None:
    """Save per-scheme CSV to data/raw/."""
    safe_name = scheme_name.replace(" ", "_").replace("/", "_")
    filename  = f"live_nav_{scheme_code}_{safe_name}.csv"
    filepath  = os.path.join(RAW_DIR, filename)
    df.to_csv(filepath, index=False)
    print(f"  💾  Saved → {filepath}")


def print_nav_summary(all_dfs: list[pd.DataFrame]) -> None:
    """Print a clean summary table of the latest NAV for each scheme."""
    print(f"\n{SEPARATOR}")
    print("  📊  LATEST NAV SUMMARY")
    print(SEPARATOR)
    print(f"  {'Scheme':<35} {'Code':>7}  {'Latest NAV':>12}  {'Date'}")
    print(f"  {'─'*35} {'─'*7}  {'─'*12}  {'─'*12}")

    for df in all_dfs:
        latest = df.iloc[-1]
        print(f"  {latest['scheme_name']:<35} "
              f"{int(latest['scheme_code']):>7}  "
              f"₹{latest['nav']:>11,.4f}  "
              f"{latest['date'].date()}")


# ── Main pipeline ─────────────────────────────────────────────────────────────

def main():
    print(f"\n{SEPARATOR}")
    print("  🚀  LIVE NAV FETCH – mfapi.in")
    print(f"  Timestamp : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(SEPARATOR)

    os.makedirs(RAW_DIR, exist_ok=True)

    all_dfs   = []
    succeeded = []
    failed    = []

    for scheme_name, scheme_code in SCHEMES.items():
        print(f"\n  [{scheme_name}]  (code: {scheme_code})")
        df = fetch_nav(scheme_name, scheme_code)

        if df is not None:
            save_individual(df, scheme_code, scheme_name)
            all_dfs.append(df)
            succeeded.append(scheme_name)
        else:
            failed.append(scheme_name)

        time.sleep(0.5)   # polite delay between API calls

    # ── Combine all into one master CSV ───────────────────────────────────────
    if all_dfs:
        combined    = pd.concat(all_dfs, ignore_index=True)
        combined_fp = os.path.join(RAW_DIR, "all_live_nav_combined.csv")
        combined.to_csv(combined_fp, index=False)

        print(f"\n{SEPARATOR}")
        print(f"  💾  Combined CSV saved → {combined_fp}")
        print(f"      Total rows : {len(combined):,}")
        print(f"      Schemes    : {combined['scheme_name'].nunique()}")

        print_nav_summary(all_dfs)

    # ── Final status ──────────────────────────────────────────────────────────
    print(f"\n{SEPARATOR}")
    print(f"  ✅  Succeeded : {len(succeeded)} scheme(s)")
    if failed:
        print(f"  ❌  Failed    : {len(failed)} → {failed}")
    print(f"  Done at {datetime.now().strftime('%H:%M:%S')}")
    print(SEPARATOR)


if __name__ == "__main__":
    main()
