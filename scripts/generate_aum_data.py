import pandas as pd

# AUM values (₹ Lakh Crore)
data = {
    "fund_house": [
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
    ],
    "2022": [8.7, 5.6, 6.4, 3.2, 2.9, 2.5, 2.7, 2.1, 1.8, 1.5],
    "2023": [9.5, 6.2, 7.1, 3.7, 3.2, 2.8, 3.0, 2.4, 2.1, 1.8],
    "2024": [10.9, 7.0, 8.3, 4.3, 3.8, 3.3, 3.4, 2.8, 2.5, 2.1],
    "2025": [12.5, 8.1, 9.5, 5.0, 4.4, 3.8, 3.9, 3.2, 2.9, 2.4]
}

df = pd.DataFrame(data)

output_file = "data/generated/aum_by_fund_house.csv"
df.to_csv(output_file, index=False)

print("=" * 50)
print("AUM DATASET GENERATED SUCCESSFULLY")
print("=" * 50)
print(df)
print("\nSaved to:", output_file)