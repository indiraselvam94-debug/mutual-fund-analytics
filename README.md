# 📊 Mutual Fund Analytics Platform
**Bluestock Fintech – Capstone Project**

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Day](https://img.shields.io/badge/Day-1%20of%207-blue)
![Python](https://img.shields.io/badge/Python-3.10%2B-green)

---

## 🎯 Project Overview

A full-stack Mutual Fund Analytics Platform built using publicly available Indian mutual fund data from **AMFI India** and **mfapi.in**.

| Metric | Value |
|--------|-------|
| AMCs covered | 10 (SBI, HDFC, ICICI, Nippon, Kotak, Axis, ABSL, UTI, Mirae, DSP) |
| Schemes | 40 |
| Daily NAV records | 46,000+ |
| SIP Inflow (Dec '25) | ₹31,002 Cr |
| AUM Anchor | SBI ₹12.5L Cr |

---

## 🗂️ Project Structure

```
mutual_fund_analytics/
├── data/
│   ├── raw/           ← Original CSV files + live NAV fetches
│   └── processed/     ← Cleaned outputs from data_ingestion.py
├── notebooks/         ← Jupyter EDA notebooks (Day 3+)
├── sql/               ← Schema DDL and queries (Day 2+)
├── dashboard/         ← Power BI / Tableau files (Day 5+)
├── reports/           ← Final PDF report and slide deck (Day 7)
├── data_ingestion.py  ← Day 1: Load & inspect 10 CSV datasets
├── live_nav_fetch.py  ← Day 1: Fetch live NAV from mfapi.in
├── requirements.txt   ← Python dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/mutual-fund-analytics.git
cd mutual-fund-analytics
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Place CSV files
Put all 10 provided CSV files into `data/raw/` with these exact names:
- `01_fund_master.csv`
- `02_nav_history.csv`
- `03_aum_by_fund_house.csv`
- `04_monthly_sip.csv`
- `05_category_inflows.csv`
- `06_folio_count.csv`
- `07_scheme_performance.csv`
- `08_transactions.csv`
- `09_holdings.csv`
- `10_benchmark.csv`

### 5. Run Day 1 scripts
```bash
# Ingest and inspect CSV files
python data_ingestion.py

# Fetch live NAV from mfapi.in
python live_nav_fetch.py
```

---

## 📅 Milestone Roadmap

| Day | Task | Status |
|-----|------|--------|
| **Day 1–2** | ETL + SQLite setup | 🔄 In Progress |
| **Day 3** | Star schema + EDA (15+ charts) | ⏳ Pending |
| **Day 4** | Risk metrics (Sharpe, Sortino, VaR) | ⏳ Pending |
| **Day 5** | Dashboard build (Power BI / Tableau) | ⏳ Pending |
| **Day 6** | Demographics + benchmark comparison | ⏳ Pending |
| **Day 7** | Docs, deck, GitHub final | ⏳ Pending |

---

## 🔑 Key Deliverables

- `O1` Python ETL pipeline (`.py` scripts)
- `O2` Star schema SQL (`schema.sql`)
- `O3` EDA notebook with 15+ charts
- `O4` Risk metrics notebook + output CSVs
- `O5` Power BI / Tableau dashboard (`.pbix` / `.twbx`)
- `O6` Demographic insights
- `O7` Benchmark comparison (Nifty 50, Nifty 100, BSE SmallCap)
- `O8` PDF report + 12-slide presentation deck

---

## 📡 Data Sources

- **mfapi.in** – Live NAV REST API
- **AMFI India** – Fund master & AUM data
- **NSE/BSE** – Benchmark index data

---

## 👤 Team

Bluestock Fintech Capstone · Individual Project  
*Due: 24 Jun 2026*
