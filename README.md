# 📊 Mutual Fund Analytics Platform
**Bluestock Fintech – Capstone Project**

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Project](https://img.shields.io/badge/Capstone-Mutual%20Fund%20Analytics-blue)
![Python](https://img.shields.io/badge/Python-3.14-green)

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

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SciPy
- SQLite
- Jupyter Notebook
- Power BI
- Git & GitHub

---

## 🗂️ Project Structure

```
mutual_fund_analytics/
├── data/
│   ├── raw/           ← Original CSV files + live NAV fetches
│   └── processed/     ← Cleaned outputs from data_ingestion.py
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb      
├── sql/               ← Schema DDL and queries (Day 2+)
├── dashboard/         ← Power BI / Tableau files (Day 5+)
├── reports/           ← Final PDF report and slide deck (Day 7)
├── data_ingestion.py  ← Day 1: Load & inspect 10 CSV datasets
├── live_nav_fetch.py  ← Day 1: Fetch live NAV from mfapi.in
├── requirements.txt   ← Python dependencies
├── fund_scorecard.csv
├── alpha_beta.csv
├── var_cvar_report.csv
├── benchmark_comparison.png
├── rolling_sharpe_chart.png
├── recommender.py
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/indiraselvam94-debug/mutual-fund-analytics.git
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

### 5. Run the project scripts
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
| Day 1 | Data Ingestion | ✅ Completed |
| Day 2 | Data Cleaning & SQLite | ✅ Completed |
| Day 3 | Exploratory Data Analysis (EDA) | ✅ Completed |
| Day 4 | Performance Analytics | ✅ Completed |
| Day 5 | Dashboard Development | ✅ Completed |
| Day 6 | Advanced Analytics | ✅ Completed |
| Day 7 | Documentation & Final Submission | ✅ Completed |

---

#

- ✅ Python ETL Pipeline
- ✅ SQLite Database & Star Schema
- ✅ Exploratory Data Analysis (EDA)
- ✅ Performance Analytics
- ✅ Advanced Analytics & Risk Metrics
- ✅ Power BI Dashboard
- ✅ Benchmark Comparison
- ✅ Final Project Report
- ✅ Presentation (PPT)

---

## 📡 Data Sources

- **mfapi.in** – Live NAV REST API
- **AMFI India** – Fund master & AUM data
- **NSE/BSE** – Benchmark index data

---

## 👤 Team

Bluestock Fintech Capstone · Individual Project
