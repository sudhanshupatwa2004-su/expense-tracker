import json

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except:
    expenses = []

def save_data():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append({"name": name, "amount": amount})
    save_data()
    print("Expense added!\n")

def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return
    
    print("\nExpenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['name']} - ₹{exp['amount']}")
    print()

def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expense: ₹{total}\n")

def delete_expense():
    view_expenses()
    if not expenses:
        return
    index = int(input("Enter number to delete: ")) - 1
    expenses.pop(index)
    save_data()
    print("Deleted!\n")

def menu():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            break
        else:
            print("Invalid choice\n")

menu()