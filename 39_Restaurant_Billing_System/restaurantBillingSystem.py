
menu_items = ["Idli", "Dosa", "Fried Rice", "Burger", "Pizza"]
menu_prices = [30, 50, 100, 80, 150]

ordered_items = []
ordered_prices = []
ordered_quantities = []


def display_menu():
    print("\n===== RESTAURANT MENU =====")

    for i in range(len(menu_items)):
        print(
            i + 1,
            menu_items[i],
            "- Rs.",
            menu_prices[i]
        )


def add_order():
    display_menu()

    choice = input("Enter item number: ")

    if not choice.isdigit():
        print("Please enter a valid item number.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(menu_items):
        print("Invalid item number.")
        return

    quantity_input = input("Enter quantity: ")

    if not quantity_input.isdigit():
        print("Please enter a valid quantity.")
        return

    quantity = int(quantity_input)

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    index = choice - 1

    ordered_items.append(menu_items[index])
    ordered_prices.append(menu_prices[index])
    ordered_quantities.append(quantity)

    print("Item added to order successfully!")


def view_order():
    if len(ordered_items) == 0:
        print("Your order is empty.")
        return

    print("\n===== YOUR ORDER =====")

    for i in range(len(ordered_items)):
        item_total = (
            ordered_prices[i] * ordered_quantities[i]
        )

        print(
            ordered_items[i],
            "x",
            ordered_quantities[i],
            "- Rs.",
            item_total
        )


def generate_bill():
    if len(ordered_items) == 0:
        print("Please add items before generating a bill.")
        return

    subtotal = 0

    print("\n========== FINAL BILL ==========")

    for i in range(len(ordered_items)):
        item_total = (
            ordered_prices[i] * ordered_quantities[i]
        )

        subtotal += item_total

        print(
            ordered_items[i],
            "x",
            ordered_quantities[i],
            "- Rs.",
            item_total
        )

    if subtotal >= 1000:
        discount_rate = 0.10
    elif subtotal >= 500:
        discount_rate = 0.05
    else:
        discount_rate = 0

    discount = subtotal * discount_rate
    final_amount = subtotal - discount

    print("--------------------------------")
    print("Subtotal: Rs.", round(subtotal, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Final Amount: Rs.", round(final_amount, 2))
    print("Thank you for visiting!")
    print("================================")


while True:
    print("\n===== RESTAURANT BILLING SYSTEM =====")
    print("1. Display Menu")
    print("2. Add Item")
    print("3. View Order")
    print("4. Generate Bill")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_menu()
    elif choice == "2":
        add_order()
    elif choice == "3":
        view_order()
    elif choice == "4":
        generate_bill()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
  
