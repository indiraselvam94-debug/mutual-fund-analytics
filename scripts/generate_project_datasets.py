import pandas as pd
import numpy as np
import random
import os

# ---------------------------------------------
# Create output folder
# ---------------------------------------------
os.makedirs("data/generated", exist_ok=True)

# ---------------------------------------------
# Fund Houses
# ---------------------------------------------
fund_houses = [
    "SBI Mutual Fund",
    "HDFC Mutual Fund",
    "ICICI Prudential Mutual Fund",
    "Nippon India Mutual Fund",
    "Kotak Mutual Fund",
    "Axis Mutual Fund",
    "Aditya Birla Sun Life Mutual Fund",
    "UTI Mutual Fund",
    "Mirae Asset Mutual Fund",
    "DSP Mutual Fund"
]

# ---------------------------------------------
# 1. AUM Dataset
# ---------------------------------------------
aum_df = pd.DataFrame({
    "fund_house": fund_houses,
    "2022":[8.7,5.6,6.4,3.2,2.9,2.5,2.7,2.1,1.8,1.5],
    "2023":[9.5,6.2,7.1,3.7,3.2,2.8,3.0,2.4,2.1,1.8],
    "2024":[10.9,7.0,8.3,4.3,3.8,3.3,3.4,2.8,2.5,2.1],
    "2025":[12.5,8.1,9.5,5.0,4.4,3.8,3.9,3.2,2.9,2.4]
})

aum_df.to_csv("data/generated/aum_by_fund_house.csv", index=False)

print("✓ AUM dataset created")

# ---------------------------------------------
# 2. Monthly SIP Dataset
# ---------------------------------------------
months = pd.date_range("2022-01-01","2025-12-01",freq="MS")

sip_values = np.linspace(11200,31002,len(months))
sip_values = sip_values + np.random.randint(-350,350,len(months))

sip_df = pd.DataFrame({
    "month":months.strftime("%Y-%m"),
    "sip_inflow_cr":sip_values.round(2)
})

# Force Dec 2025 value
sip_df.loc[sip_df.index[-1],"sip_inflow_cr"] = 31002

sip_df.to_csv(
    "data/generated/monthly_sip.csv",
    index=False
)

print("✓ Monthly SIP dataset created")
# ---------------------------------------------
# 3. Category Inflow Dataset
# ---------------------------------------------
categories = [
    "Large Cap",
    "Mid Cap",
    "Small Cap",
    "Flexi Cap",
    "ELSS",
    "Hybrid",
    "Debt",
    "Liquid"
]

months = pd.date_range("2022-01-01", "2025-12-01", freq="MS")

rows = []

for month in months:
    for category in categories:
        rows.append({
            "month": month.strftime("%Y-%m"),
            "category": category,
            "net_inflow_cr": random.randint(500, 8000)
        })

category_df = pd.DataFrame(rows)

category_df.to_csv(
    "data/generated/category_inflows.csv",
    index=False
)

print("✓ Category inflow dataset created")

# ---------------------------------------------
# 4. Folio Count Dataset
# ---------------------------------------------
months = pd.date_range("2022-01-01", "2025-12-01", freq="MS")

folio = np.linspace(13.26, 26.12, len(months))

folio_df = pd.DataFrame({
    "month": months.strftime("%Y-%m"),
    "folio_count_cr": folio.round(2)
})

folio_df.to_csv(
    "data/generated/folio_count.csv",
    index=False
)

print("✓ Folio count dataset created")
# ---------------------------------------------
# 5. Scheme Performance Dataset
# ---------------------------------------------
schemes = [
    "SBI Bluechip Direct",
    "HDFC Top 100 Direct",
    "ICICI Pru Bluechip Direct",
    "Nippon Large Cap Direct",
    "Kotak Bluechip Direct",
    "Axis Bluechip Direct",
    "ABSL Frontline Equity Direct",
    "UTI Flexi Cap Direct",
    "Mirae Asset Large Cap Direct",
    "DSP Top 100 Equity Direct"
]

categories = [
    "Large Cap",
    "Large Cap",
    "Large Cap",
    "Large Cap",
    "Large Cap",
    "Large Cap",
    "Large Cap",
    "Flexi Cap",
    "Large Cap",
    "Large Cap"
]

performance_rows = []

for i in range(len(schemes)):
    performance_rows.append({
        "scheme_name": schemes[i],
        "category": categories[i],
        "return_1y": round(random.uniform(8, 25), 2),
        "return_3y": round(random.uniform(10, 22), 2),
        "return_5y": round(random.uniform(11, 20), 2),
        "expense_ratio": round(random.uniform(0.45, 2.20), 2),
        "risk_level": random.choice(["Low", "Moderate", "High"])
    })

performance_df = pd.DataFrame(performance_rows)

performance_df.to_csv(
    "data/generated/scheme_performance.csv",
    index=False
)

print("✓ Scheme performance dataset created")
# ---------------------------------------------
# 6. Investor Transactions Dataset
# ---------------------------------------------
states = [
    "Tamil Nadu",
    "Karnataka",
    "Maharashtra",
    "Delhi",
    "Gujarat",
    "Kerala",
    "Telangana",
    "Andhra Pradesh",
    "West Bengal",
    "Rajasthan",
    "Punjab",
    "Uttar Pradesh"
]

age_groups = [
    "18-25",
    "26-35",
    "36-45",
    "46-60",
    "60+"
]

genders = [
    "Male",
    "Female"
]

transaction_types = [
    "SIP",
    "Lumpsum",
    "Redemption"
]

city_tiers = [
    "T30",
    "B30"
]

dates = pd.date_range("2022-01-01", "2025-12-31", freq="D")

transactions = []

for i in range(32000):
    transactions.append({
        "transaction_id": i + 1,
        "date": random.choice(dates).strftime("%Y-%m-%d"),
        "scheme_name": random.choice(schemes),
        "transaction_type": random.choices(
            transaction_types,
            weights=[65, 20, 15]
        )[0],
        "amount": random.randint(500, 500000),
        "state": random.choice(states),
        "age_group": random.choice(age_groups),
        "gender": random.choice(genders),
        "city_tier": random.choices(
            city_tiers,
            weights=[70, 30]
        )[0]
    })

transactions_df = pd.DataFrame(transactions)

transactions_df.to_csv(
    "data/generated/investor_transactions.csv",
    index=False
)

print("✓ Investor Transactions dataset created")
# ---------------------------------------------
# 7. Portfolio Holdings Dataset
# ---------------------------------------------
sectors = [
    "Banking",
    "IT",
    "Pharma",
    "Auto",
    "FMCG",
    "Energy",
    "Metals",
    "Telecom",
    "Healthcare",
    "Infrastructure"
]

holdings = []

for scheme in schemes:

    # Generate random weights
    weights = np.random.dirichlet(np.ones(len(sectors)), size=1)[0] * 100

    for sector, weight in zip(sectors, weights):
        holdings.append({
            "scheme_name": scheme,
            "sector": sector,
            "weight_percent": round(weight, 2)
        })

holdings_df = pd.DataFrame(holdings)

holdings_df.to_csv(
    "data/generated/portfolio_holdings.csv",
    index=False
)

print("✓ Portfolio Holdings dataset created")

# ---------------------------------------------
# FINAL REPORT
# ---------------------------------------------
print("\n" + "="*50)
print("ALL PROJECT DATASETS GENERATED SUCCESSFULLY")
print("="*50)

files = [
    "aum_by_fund_house.csv",
    "monthly_sip.csv",
    "category_inflows.csv",
    "folio_count.csv",
    "scheme_performance.csv",
    "investor_transactions.csv",
    "portfolio_holdings.csv"
]

print("\nGenerated files:")

for f in files:
    print("✓", f)

print("\nLocation: data/generated/")
print("="*50)