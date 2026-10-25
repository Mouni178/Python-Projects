
employee_names = []
employee_ids = []
basic_salaries = []


def add_employee():
    employee_id = input("Enter employee ID: ").strip()

    if employee_id == "":
        print("Employee ID cannot be empty.")
        return

    if employee_id in employee_ids:
        print("Employee ID already exists.")
        return

    name = input("Enter employee name: ").strip()

    if name == "":
        print("Employee name cannot be empty.")
        return

    salary_input = input("Enter basic monthly salary: ")

    if not salary_input.replace(".", "", 1).isdigit():
        print("Enter a valid salary.")
        return

    salary = float(salary_input)

    if salary <= 0:
        print("Salary must be greater than zero.")
        return

    employee_ids.append(employee_id)
    employee_names.append(name)
    basic_salaries.append(salary)

    print("Employee added successfully!")


def calculate_salary(index):
    basic = basic_salaries[index]

    hra = basic * 0.20
    allowance = basic * 0.10
    deduction = basic * 0.05

    gross_salary = basic + hra + allowance
    net_salary = gross_salary - deduction

    return hra, allowance, deduction, gross_salary, net_salary


def generate_payslip(index):
    hra, allowance, deduction, gross, net = calculate_salary(index)

    print("\n========== EMPLOYEE PAYSLIP ==========")
    print("Employee ID:", employee_ids[index])
    print("Employee Name:", employee_names[index])
    print("--------------------------------------")
    print("Basic Salary: Rs.", round(basic_salaries[index], 2))
    print("HRA (20%): Rs.", round(hra, 2))
    print("Other Allowance (10%): Rs.", round(allowance, 2))
    print("Gross Salary: Rs.", round(gross, 2))
    print("Deduction (5%): Rs.", round(deduction, 2))
    print("--------------------------------------")
    print("Net Salary: Rs.", round(net, 2))
    print("======================================")


def view_all_employees():
    if len(employee_ids) == 0:
        print("No employee records available.")
        return

    print("\n===== EMPLOYEE PAYROLL LIST =====")

    for i in range(len(employee_ids)):
        hra, allowance, deduction, gross, net = calculate_salary(i)

        print(
            employee_ids[i],
            "|",
            employee_names[i],
            "| Net Salary: Rs.",
            round(net, 2)
        )


def search_employee():
    employee_id = input("Enter employee ID to search: ").strip()

    if employee_id in employee_ids:
        index = employee_ids.index(employee_id)
        generate_payslip(index)
    else:
        print("Employee not found.")


def calculate_total_payroll():
    total = 0

    for i in range(len(employee_ids)):
        salary_details = calculate_salary(i)
        net_salary = salary_details[4]
        total += net_salary

    print("Total Net Payroll: Rs.", round(total, 2))


while True:
    print("\n===== EMPLOYEE PAYROLL SYSTEM =====")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Generate Payslip")
    print("4. Search Employee")
    print("5. Calculate Total Payroll")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_all_employees()
    elif choice == "3":
        if len(employee_ids) == 0:
            print("No employees available.")
        else:
            employee_id = input("Enter employee ID: ").strip()

            if employee_id in employee_ids:
                index = employee_ids.index(employee_id)
                generate_payslip(index)
            else:
                print("Employee not found.")
    elif choice == "4":
        search_employee()
    elif choice == "5":
        calculate_total_payroll()
    elif choice == "6":
        print("Thank you for using Payroll Management System!")
        break
    else:
        print("Invalid choice. Try again.")
  
