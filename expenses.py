from expenses_database import init_db, add_expense, get_expenses
from datetime import date

init_db()

def get_amount():
    while True:
        amount_str = input("Add expense amount: ")
        try:
            return float(amount_str)
        except ValueError:
            print("Amount must be a number!")

def menu():
    while True:
        print("\n EXPENSES TRACKING SYSTEM")
        print("1. ADD AN EXPENSE ")
        print("2. VIEW EXPENSES")
        print("3. REPORTS")
        print("4. CANCEL")

        choice = input("WELCOME! PLEASE CHOOSE AN OPTION\n")

        if choice == "1":
            amount = get_amount()
            type = input("Type of expense: ")
            description = input("Description: ")
            timestamp = date.today().isoformat()
            add_expense(amount, type, description, timestamp)
            print("EXPENSE ADDED SUCCESSFULLY!" )
        elif choice == "2":
            expenses = get_expenses()
            for e in expenses:
                print(expenses)
        elif choice == "3":
            print("REPORTS FEATURE COMING SOON...")
        elif choice == "4":
            break
        else:
            print("INVALID CHOICE. 404 - CHOICE NOT FOUND ;)")

if __name__ == "__main__":
    menu()
