from db import connect

def add_expense(expense):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
        expense.to_tuple()
    )

    conn.commit()
    conn.close()

def view_expenses():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    conn.close()
    return rows
