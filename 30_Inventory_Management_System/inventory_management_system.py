
products = []
prices = []
quantities = []


def add_product():
    name = input("Enter product name: ").strip()

    if name == "":
        print("Product name cannot be empty.")
        return

    for product in products:
        if product.lower() == name.lower():
            print("Product already exists.")
            return

    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    if price <= 0 or quantity < 0:
        print("Enter a valid price and quantity.")
        return

    products.append(name)
    prices.append(price)
    quantities.append(quantity)

    print("Product added successfully!")


def view_products():
    if len(products) == 0:
        print("No products available.")
        return

    print("\n===== INVENTORY =====")

    for i in range(len(products)):
        print("Product:", products[i])
        print("Price: Rs.", prices[i])
        print("Quantity:", quantities[i])
        print("--------------------")


def search_product():
    name = input("Enter product name to search: ").strip().lower()

    for i in range(len(products)):
        if products[i].lower() == name:
            print("Product:", products[i])
            print("Price: Rs.", prices[i])
            print("Quantity:", quantities[i])
            return

    print("Product not found.")


def update_quantity():
    name = input("Enter product name: ").strip().lower()

    for i in range(len(products)):
        if products[i].lower() == name:
            quantity = int(input("Enter quantity to add: "))

            if quantity <= 0:
                print("Quantity must be positive.")
                return

            quantities[i] += quantity
            print("Stock updated successfully!")
            return

    print("Product not found.")


def sell_product():
    name = input("Enter product name to sell: ").strip().lower()

    for i in range(len(products)):
        if products[i].lower() == name:
            quantity = int(input("Enter quantity to sell: "))

            if quantity <= 0:
                print("Enter a valid quantity.")
            elif quantity > quantities[i]:
                print("Insufficient stock.")
            else:
                quantities[i] -= quantity
                total = quantity * prices[i]

                print("Sale successful!")
                print("Product:", products[i])
                print("Quantity sold:", quantity)
                print("Total amount: Rs.", round(total, 2))

            return

    print("Product not found.")


def calculate_inventory_value():
    total = 0

    for i in range(len(products)):
        total += prices[i] * quantities[i]

    print("Total Inventory Value: Rs.", round(total, 2))


while True:
    print("\n===== INVENTORY MANAGEMENT =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Sell Product")
    print("6. Calculate Inventory Value")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_quantity()
    elif choice == "5":
        sell_product()
    elif choice == "6":
        calculate_inventory_value()
    elif choice == "7":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
          
