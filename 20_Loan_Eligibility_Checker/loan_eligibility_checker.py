print("LOAN ELIGIBILITY CHECKER")

name = input("Enter your name: ")
salary = float(input("Enter your monthly salary: "))
expenses = float(input("Enter your monthly expenses: "))
credit_score = int(input("Enter your credit score: "))
loan_amount = float(input("Enter requested loan amount: "))

monthly_savings = salary - expenses

print("\n===== FINANCIAL DETAILS =====")

print("Name:", name)
print("Monthly Salary: ", salary)
print("Monthly Expenses:", expenses)
print("Monthly Savings:", monthly_savings)
print("Credit Score:", credit_score)
print("Requested Loan: ", loan_amount)

print("ELIGIBILITY RESULT")

if salary <= 0 or expenses < 0 or loan_amount <= 0:
    print("Please enter valid financial details.")

elif expenses >= salary:
    print("Not Eligible")
    print("Reason: Monthly expenses are equal to or greater than salary.")

elif credit_score < 650:
    print("Not Eligible")
    print("Reason: Credit score is below the required level.")

elif loan_amount > salary * 20:
    print("Not Eligible")
    print("Reason: Requested loan amount is too high.")

else:
    print("Eligible for further consideration.")
