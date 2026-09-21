accounts = {}
transactions = []


def create_account():
    name = input("Enter account holder name: ")
    account_number = input("Enter account number: ")

    if account_number in accounts:
        print("Account already exists.")
        return

    accounts[account_number] = {
        "name": name,
        "balance": 0
    }

    print("Account created successfully.")


def check_balance():
    account_number = input("Enter account number: ")

    if account_number in accounts:
        print("Account Holder:", accounts[account_number]["name"])
        print("Balance: ₹", accounts[account_number]["balance"])
    else:
        print("Account not found.")


def deposit_money():
    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Enter a valid amount.")
        return

    accounts[account_number]["balance"] += amount

    transactions.append(
        account_number + " deposited ₹" + str(amount)
    )

    print("Money deposited successfully.")


def withdraw_money():
    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Enter a valid amount.")

    elif amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")

    else:
        accounts[account_number]["balance"] -= amount

        transactions.append(
            account_number + " withdrew ₹" + str(amount)
        )

        print("Please collect your money.")


def transfer_money():
    sender = input("Enter sender account number: ")
    receiver = input("Enter receiver account number: ")

    if sender not in accounts:
        print("Sender account not found.")
        return

    if receiver not in accounts:
        print("Receiver account not found.")
        return

    amount = float(input("Enter transfer amount: "))

    if amount <= 0:
        print("Enter a valid amount.")

    elif amount > accounts[sender]["balance"]:
        print("Insufficient balance.")

    else:
        accounts[sender]["balance"] -= amount
        accounts[receiver]["balance"] += amount

        transactions.append(
            sender + " transferred ₹" + str(amount)
            + " to " + receiver
        )

        print("Money transferred successfully.")


def transaction_history():
    if len(transactions) == 0:
        print("No transactions found.")
    else:
        print("\n===== TRANSACTION HISTORY =====")

        for transaction in transactions:
            print(transaction)


def account_details():
    account_number = input("Enter account number: ")

    if account_number in accounts:
        print("\n===== ACCOUNT DETAILS =====")
        print("Account Number:", account_number)
        print("Account Holder:", accounts[account_number]["name"])
        print("Balance: ₹", accounts[account_number]["balance"])
    else:
        print("Account not found.")


while True:

    print("\n===== PERSONAL BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Transfer Money")
    print("6. Transaction History")
    print("7. Account Details")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        check_balance()

    elif choice == "3":
        deposit_money()

    elif choice == "4":
        withdraw_money()

    elif choice == "5":
        transfer_money()

    elif choice == "6":
        transaction_history()
