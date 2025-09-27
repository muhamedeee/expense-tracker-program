import random
from datetime import date
from expenses_database import add_expense, get_expenses

types = ["Food", "Gas", "Bills", "Travel", "Shopping"]

for i in range(5):
    amount = round(random.uniform(1, 100), 2)
    type = random.choice(types)
    description = f"Automatic testing bot {i+1}"
    add_expense(amount, type, description, date.today().isoformat())

print(get_expenses())
