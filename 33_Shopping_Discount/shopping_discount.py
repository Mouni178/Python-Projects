prices = []

def add_product():
    price = float(input("Enter product price: "))

    if price <= 0:
        print("Enter a valid price.")
        return

    prices.append(price)
    print("Product added successfully!")


def view_bill():
    if len(prices) == 0:
        print("No products added.")
        return

    total = sum(prices)

    if total >= 5000:
        discount_rate = 0.15
    elif total >= 3000:
        discount_rate = 0.10
    elif total >= 1000:
        discount_rate = 0.05
    else:
        discount_rate = 0

    discount = total * discount_rate
    final_amount = total - discount

    print("\n===== SHOPPING BILL =====")

    for i in range(len(prices)):
        print("Product", i + 1, "- Rs.", prices[i])

    print("-------------------------")
    print("Original Amount: Rs.", round(total, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Final Amount: Rs.", round(final_amount, 2))
    print("Total Savings: Rs.", round(discount, 2))


while True:
    print("\n===== DISCOUNT CALCULATOR =====")
    print("1. Add Product")
    print("2. View Final Bill")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_bill()
    elif choice == "3":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice.")
