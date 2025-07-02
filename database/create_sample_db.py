import sqlite3
import pandas as pd

conn = sqlite3.connect("database/sample.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER,
    join_date TEXT
)
""")

df = pd.DataFrame([
    (1, 'Alice', 'HR', 50000, '2020-01-15'),
    (2, 'Bob', 'IT', 70000, '2019-03-22'),
    (3, 'Charlie', 'Finance', 65000, '2021-06-10'),
    (4, 'David', 'IT', 72000, '2018-11-05'),
    (5, 'Eve', 'HR', 52000, '2022-08-19'),
], columns=["id", "name", "department", "salary", "join_date"])

df.to_sql("employees", conn, if_exists="replace", index=False)
conn.commit()
conn.close()
