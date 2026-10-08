def calculate_bill(units):

    if units <= 100:
        bill = units * 1.50

    elif units <= 200:
        bill = (100 * 1.50) + ((units - 100) * 2.50)

    elif units <= 500:
        bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)

    else:
        bill = (
            (100 * 1.50)
            + (100 * 2.50)
            + (300 * 4.00)
            + ((units - 500) * 6.00)
        )

    return bill


print("===== ELECTRICITY BILL CALCULATOR =====")

name = input("Enter customer name: ")
units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Units cannot be negative.")

else:
    energy_charge = calculate_bill(units)
    fixed_charge = 100
    total_bill = energy_charge + fixed_charge

    print("\n===== ELECTRICITY BILL =====")
    print("Customer Name:", name)
    print("Units Consumed:", units)
    print("Energy Charge: ₹", round(energy_charge, 2))
    print("Fixed Charge: ₹", fixed_charge)
    print("Total Bill: ₹", round(total_bill, 2))
