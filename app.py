import streamlit as st
from expense import Expenses
from utils import add_expense, view_expenses
from analytics import analyze_expenses_df
from ai_insights import generate_insights
from finance_api import get_stock_data
from db import create_table

create_table()

st.title(" 💰 Smart Expense Tracker AI")

menu = st.sidebar.selectbox(
    "Menu", ["Add Expense", "View Expenses", "Analytics", "AI Insights", "Finance"]
)

# ---------------- ADD EXPENSE ----------------
if menu == "Add Expense":
    title = st.text_input("Title")
    amount = st.number_input("Amount")
    category = st.text_input("Category")
    date = st.date_input("Date")

    if st.button("Add"):
        exp = Expenses(title, amount, category, str(date))
        add_expense(exp)
        st.success("Expense Added!")

# ---------------- VIEW EXPENSES ----------------
elif menu == "View Expenses":
    data = view_expenses()
    st.write(data)

# ---------------- ANALYTICS ----------------
elif menu == "Analytics":
    df = analyze_expenses_df()
    st.write(df)

    if not df.empty:
        # ✅ Fix: normalize column names
        df.columns = df.columns.str.strip().str.lower()

        # ✅ Safe check before using
        if "category" in df.columns and "amount" in df.columns:
            chart_data = df.groupby("category")["amount"].sum()
            st.bar_chart(chart_data)
        else:
            st.error(f"Required columns not found. Available columns: {list(df.columns)}")

# ---------------- AI INSIGHTS ----------------
elif menu == "AI Insights":
    df = analyze_expenses_df()

    if not df.empty:
        df.columns = df.columns.str.strip().str.lower()  # keep consistent
        insights = generate_insights(df)
        st.write(insights)
    else:
        st.warning("No data available")

# ---------------- FINANCE ----------------
elif menu == "Finance":
    ticker = st.text_input("Enter Stock (e.g., AAPL)")

    if st.button("Fetch"):
        df = get_stock_data(ticker)

        if df is not None and not df.empty:
            st.line_chart(df["Close"])
        else:
            st.error("No stock data found.")
