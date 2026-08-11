#Expense Tracker Project

expenses = [] # list of all expenses in form of dictionaries
print("Welcome to the Expense Tracker : ")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. view Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    #ADD EXPENSE

    if choice == "1":
        date = input("Enter the date: ")
        category = input("Enter the category (e.g., Food, Transport, Makeup): ")
        description = input("Enter the description: ")
        amount = float(input("Enter the amount: "))
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expenses.append(expense)
        print("\nExpense added successfully.")

    elif choice == "2":
        # View Expenses
        if len(expenses) == 0:
            print("No expenses found. :)")
        else:
            print("\nHere are your expenses:")
            for idx, expense in enumerate(expenses, 1):
                print(f"Expense no: {idx}")
                print(f"  Date: {expense['date']}")
                print(f"  Category: {expense['category']}")
                print(f"  Description: {expense['description']}")
                print(f"  Amount: {expense['amount']:.2f}")

    elif choice == "3":
        # View Total Expenses
        total = sum(expense['amount'] for expense in expenses)
        print(f"\nTotal Expenses: {total:.2f}")

    elif choice == "4":
        # Exit
        print("Thank you for using the EXPENSE TRACKER. Have a great day!")
        break

    else:
        print("Invalid choice. Try Again.")