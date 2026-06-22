import pandas as pd
import sqlite3

conn = sqlite3.connect("data/db/nifty100.db")

companies = pd.read_excel("data/raw/companies.xlsx")
companies.to_sql("companies", conn, if_exists="replace", index=False)

profitandloss = pd.read_excel("data/raw/profitandloss.xlsx")
profitandloss.to_sql("profitandloss", conn, if_exists="replace", index=False)

balancesheet = pd.read_excel("data/raw/balancesheet.xlsx")
balancesheet.to_sql("balancesheet", conn, if_exists="replace", index=False)

cashflow = pd.read_excel("data/raw/cashflow.xlsx")
cashflow.to_sql("cashflow", conn, if_exists="replace", index=False)

print("Data Loaded Successfully")

conn.close()