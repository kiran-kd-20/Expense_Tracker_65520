import datetime

expenses = []

def add_expense():
    print("\nAdd New Expense")
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please try again.")
    category = input("Enter category: ").strip()
    while True:
        amount_str = input("Enter amount: ")
        try:
            amount = float(amount_str)
            if amount < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid amount. Please enter a positive number.")
    description = input("Enter description: ").strip()
    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    })
    print("Expense added successfully.\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    print("\nAll Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['date']} | {exp['category']} | ${exp['amount']:.2f} | {exp['description']}")
    print()

def total_by_category():
    if not expenses:
        print("No expenses recorded.\n")
        return
    category = input("Enter category to calculate total: ").strip()
    total = sum(exp['amount'] for exp in expenses if exp['category'].lower() == category.lower())
    print(f"Total expenses for category '{category}': ${total:.2f}\n")

def delete_expense():
    if not expenses:
        print("No expenses to delete.\n")
        return
    view_expenses()
    while True:
        idx_str = input("Enter the expense number to delete: ")
        if idx_str.isdigit():
            idx = int(idx_str)
            if 1 <= idx <= len(expenses):
                removed = expenses.pop(idx - 1)
                print(f"Deleted expense: {removed['category']} - ${removed['amount']:.2f} on {removed['date']}\n")
                break
            else:
                print("Invalid expense number. Try again.")
        else:
            print("Please enter a valid number.")

def main_menu():
    while True:
        print("==== Simple Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Expenses by Category")
        print("4. Delete an Expense")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main_menu()
