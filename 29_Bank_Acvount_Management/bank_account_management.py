
balance = 0
transactions = []
account_created = False
account_holder = ""

def create_account():
    global account_created, account_holder

    if account_created:
        print("Account already exists.")
        return

    account_holder = input("Enter account holder name: ").strip()

    if account_holder == "":
        print("Name cannot be empty.")
        return

    account_created = True
    print("Bank account created successfully!")


def deposit_money():
    global balance

    if not account_created:
        print("Please create an account first.")
        return

    amount = float(input("Enter deposit amount: "))

    if amount <= 0:
        print("Enter a valid amount.")
        return

    balance += amount
    transactions.append("Deposited: Rs. " + str(amount))
    print("Money deposited successfully.")


def withdraw_money():
    global balance

    if not account_created:
        print("Please create an account first.")
        return

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        transactions.append("Withdrawn: Rs. " + str(amount))
        print("Withdrawal successful.")


def check_balance():
    if not account_created:
        print("Please create an account first.")
        return

    print("Account Holder:", account_holder)
    print("Current Balance: Rs.", round(balance, 2))


def view_transactions():
    if not account_created:
        print("Please create an account first.")
        return

    if len(transactions) == 0:
        print("No transactions found.")
    else:
        print("\n===== TRANSACTION HISTORY =====")

        for transaction in transactions:
            print(transaction)


while True:
    print("\n===== BANK ACCOUNT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View Transactions")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        view_transactions()
    elif choice == "6":
        print("Thank you for using the Bank Account System!")
        break
    else:
        print("Invalid choice. Try again.")
  
