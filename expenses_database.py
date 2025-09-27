import sqlite3
import csv

db_name = "expenses.db"

# Initializes database
def init_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        type TEXT,
        description TEXT,
        date TEXT
        )"""
    )
    conn.commit()
    conn.close()

# Runs query to insert rows and columns
def add_expense(amount, type, description, date):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(
        "INSERT INTO expenses (amount, type, description, date) VALUES (?, ?, ?, ?)",
        (amount, type, description, date),
    )
    conn.commit()
    conn.close()

# Fetches data and stores in a list; returns list
def get_expenses():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    rows = c.fetchall()
    conn.close()
    return rows

def get_total():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT SUM(amount) FROM expenses")
    total = c.fetchone()[0]
    conn.close()
    return total if total else 0.0

def get_by_type():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT type, SUM(amount) FROM expenses GROUP BY type")
    result = c.fetchall()
    conn.close
    return result
