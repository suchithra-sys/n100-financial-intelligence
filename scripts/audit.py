import pandas as pd
import sqlite3
import os

conn = sqlite3.connect("data/db/nifty100.db")

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow"
]

audit = []

for table in tables:
    count = pd.read_sql(
        f"SELECT COUNT(*) as rows FROM {table}",
        conn
    )

    audit.append([table, count.iloc[0, 0]])

audit_df = pd.DataFrame(
    audit,
    columns=["table_name", "row_count"]
)

os.makedirs("output", exist_ok=True)

audit_df.to_csv(
    "output/load_audit.csv",
    index=False
)

print(audit_df)

conn.close()