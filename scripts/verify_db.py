import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

query = "SELECT COUNT(*) as total_rows FROM fact_nav"

result = pd.read_sql(query, conn)

print(result)

conn.close()