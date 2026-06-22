import pandas as pd
import sqlite3
import os

conn = sqlite3.connect("data/db/nifty100.db")

results = []

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow"
]

for table in tables:
    try:
        count = pd.read_sql(
            f"SELECT COUNT(*) AS cnt FROM {table}",
            conn
        ).iloc[0, 0]

        if count == 0:
            results.append([
                f"DQ_{table}",
                "CRITICAL",
                table,
                "Table is empty",
                count
            ])
        else:
            results.append([
                f"DQ_{table}",
                "PASS",
                table,
                "Data loaded successfully",
                count
            ])

    except Exception as e:
        results.append([
            f"DQ_{table}",
            "CRITICAL",
            table,
            str(e),
            0
        ])

validation_df = pd.DataFrame(
    results,
    columns=[
        "rule_id",
        "severity",
        "table_name",
        "message",
        "record_count"
    ]
)

os.makedirs("output", exist_ok=True)

validation_df.to_csv(
    "output/validation_failures.csv",
    index=False
)

print(validation_df)

conn.close()

print("\nValidation report generated successfully.")