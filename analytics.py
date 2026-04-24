import pandas as pd
from db import connect

def analyze_expenses_df():
    conn = connect()
    df = pd.read_sql_query("SELECT * FROM expenses",conn)
    conn.close()
    return df

#streamlit run app.py
