expenses=[]
def add_expenses():
  description=input("Enter Expense name:")
  amount=float(input("Enter amount:")
  expenses.append(expense)
  amounts.append(amount)
  print("Expense added Successfully")
def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("Your Expenses")
        for i in range(len(expenses)):
            print(i + 1, expenses[i],amounts[i],"rupees")
def total_expenses():
    total = 0
    for amount in amounts:
        total = total + amount
    print("Total Expenses: ₹", total)
while True:
    print("1.add Expense")
    print("2.View Expenses")
    print("3.Total Expenses")
    print("4.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")


