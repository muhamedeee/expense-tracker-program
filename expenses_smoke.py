import unittest
import sqlite3
from expenses_database import init_db, add_expense, get_total, get_by_type

class SmokeTestExpenses(unittest.TestCase):
    def setUp(self):
        init_db()
        conn = sqlite3.connect("expenses.db")
        c = conn.cursor()
        c.execute("DELETE FROM expenses")
        conn.commit()
        conn.close()

    def test_add(self):
        try:
            add_expense(100, "Gas", "Cash", "27-09-2025")
        except Exception as i:
            self.fail(f"add_expense crashed: {i}")

    def test_total(self):
        add_expense(100, "Food", "Card", "01-01-2025"); add_expense(34, "Gas", "Cash", "02-05-2025")
        total = get_total()
        self.assertEqual(total, 134)

    def test_type(self):
        add_expense(100, "Food", "Card", "01-01-2025"); add_expense(34, "Gas", "Cash", "02-05-2025")
        type = get_by_type()
        types = [j[0] for j in type]
        self.assertIn("Food", types)
        self.assertIn("Gas", types)

if __name__ == "__main__":
    unittest.main()
