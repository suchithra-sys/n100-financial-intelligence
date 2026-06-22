import sqlite3

conn = sqlite3.connect("data/db/nifty100.db")

with open("sql/schema.sql","r") as f:
    conn.executescript(f.read())

conn.commit()
conn.close()

print("Database Created")