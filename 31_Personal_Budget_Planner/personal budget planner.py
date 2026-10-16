categories = []
amounts = []

def add_expense():
    category = input("Enter expense category: ").strip()

    if category == "":
        print("Category cannot be empty.")
        return

    amount = float(input("Enter expense amount: "))

    if amount <= 0:
        print("Enter a valid amount.")
        return

    categories.append(category)
    amounts.append(amount)

    print("Expense added successfully!")


def view_expenses():
    if len(categories) == 0:
        print("No expenses recorded.")
        return

    print("\n===== EXPENSE DETAILS =====")

    for i in range(len(categories)):
        print(i + 1, categories[i], "- Rs.", amounts[i])


def calculate_budget(income):
    total = sum(amounts)
    remaining = income - total

    print("\n===== MONTHLY BUDGET =====")
    print("Monthly Income: Rs.", income)
    print("Total Expenses: Rs.", round(total, 2))
    print("Remaining Balance: Rs.", round(remaining, 2))

    if remaining > 0:
        print("You are within your budget.")
    elif remaining == 0:
        print("You have used your entire budget.")
    else:
        print("You have exceeded your budget.")


def highest_expense():
    if len(amounts) == 0:
        print("No expenses available.")
        return

    highest = max(amounts)
    index = amounts.index(highest)

    print("Highest Expense:", categories[index])
    print("Amount: Rs.", highest)


print("===== PERSONAL BUDGET PLANNER =====")

income = float(input("Enter monthly income: "))

if income <= 0:
    print("Please enter a valid income.")
else:
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Budget")
        print("4. Find Highest Expense")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_budget(income)
        elif choice == "4":
            highest_expense()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")
