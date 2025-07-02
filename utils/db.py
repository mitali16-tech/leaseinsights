import sqlite3
import pandas as pd

def run_query(sql: str):
    conn = sqlite3.connect("database/sample.db")
    try:
        df = pd.read_sql_query(sql, conn)
        return df
    except Exception as e:
        return f"Error: {str(e)}"
