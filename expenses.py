from expenses_database import init_db, add_expense, get_expenses, get_total, get_by_type
from datetime import date

init_db()

def get_amount():
    while True:
        amount_str = input("Add expense amount: ")
        try:
            return float(amount_str)
        except ValueError:
            print("Amount must be a number!")

def get_report():
    while True:
        print("\n ---REPORTS---")
        print("1. TOTAL EXPENSES REPORT")
        print("2. EXPENSES BY TYPE REPORT")
        print("3. MAIN MENU")

        choice = input("CHOOSE AN OPTION: ")

        if choice == "1":
            total = get_total()
            print(f"Total spent: {total:.2f} BAM")
        elif choice == "2":
            report_by_type = get_by_type()
            for i, amount in report_by_type:
                print(f"{i}: {amount: .2f} BAM")
        else:
            break

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
            get_report()
        elif choice == "4":
            break
        else:
            print("INVALID CHOICE. 404 - CHOICE NOT FOUND ;)")

if __name__ == "__main__":
    menu()
