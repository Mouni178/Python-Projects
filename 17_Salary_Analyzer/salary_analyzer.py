salaries = []


def add_salaries():
    number = int(input("Enter number of employees: "))

    for i in range(number):
        salary = float(input("Enter salary: "))

        if salary > 0:
            salaries.append(salary)
        else:
            print("Salary must be greater than 0.")


def analyze_salaries():
    if len(salaries) == 0:
        print("No salary data available.")
        return

    total = sum(salaries)
    average = total / len(salaries)
    highest = max(salaries)
    lowest = min(salaries)

    above_average = 0

    for salary in salaries:
        if salary > average:
            above_average += 1

    print("\n===== SALARY ANALYSIS =====")

    print("Salaries:", salaries)
    print("Total Salary:", total)
    print("Average Salary:", round(average, 2))
    print("Highest Salary:", highest)
    print("Lowest Salary:", lowest)
    print("Employees Above Average:", above_average)


print("===== EMPLOYEE SALARY ANALYZER =====")

add_salaries()
analyze_salaries()
