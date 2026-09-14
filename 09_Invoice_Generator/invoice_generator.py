items = []
quantities = []
prices = []


def add_item():
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    items.append(item)
    quantities.append(quantity)
    prices.append(price)

    print("Item added successfully!")


def show_invoice(customer_name):
    print("\n========== INVOICE ==========")
    print("Customer:", customer_name)
    print("-----------------------------")

    subtotal = 0

    for i in range(len(items)):
        item_total = quantities[i] * prices[i]
        subtotal += item_total

        print(
            i + 1,
            items[i],
            "x", quantities[i],
            "₹", item_total
        )

    print("-----------------------------")
    print("Subtotal: ₹", subtotal)

    if subtotal >= 5000:
        discount = subtotal * 0.10
    elif subtotal >= 2000:
        discount = subtotal * 0.05
    else:
        discount = 0

    final_amount = subtotal - discount

    print("Discount: ₹", discount)
    print("Final Amount: ₹", final_amount)
    print("=============================")


print("===== INVOICE GENERATOR =====")

customer_name = input("Enter customer name: ")

while True:

    print("\n1. Add Item")
    print("2. Generate Invoice")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        if len(items) == 0:
            print("No items added.")
        else:
            show_invoice(customer_name)

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
