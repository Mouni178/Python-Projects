balance = 10000
transactions = []
def check_balance():
    print("Current Balance: ", balance)
def deposit():
    global balance
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        balance = balance + amount
        transactions.append("Deposited " + str(amount))
        print("Amount deposited successfully!")
    else:
        print("Enter a valid amount.")
def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance = balance - amount
        transactions.append("Withdrawn " + str(amount))
        print("Please collect your cash.")
def view_transactions():
    if len(transactions) == 0:
        print("No transactions found.")
    else:
        print("TRANSACTIONS")
        for transaction in transactions:
            print(transaction)
while True:
    print("\n===== ATM SIMULATOR =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Transactions")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        view_transactions()
    elif choice == "5":
        print("Thank you for using the ATM!")
        break
    else:
        print("Invalid choice. Please try again.")
