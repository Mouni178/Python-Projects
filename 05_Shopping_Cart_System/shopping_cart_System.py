products = {
    "laptop": 50000,
    "headphones": 2000,
    "mouse": 800,
    "keyboard": 1500,
    "usb cable": 300
}

cart = []


def view_products():
    print("\n===== AVAILABLE PRODUCTS =====")

    for product, price in products.items():
        print(product, "₹", price)


def add_to_cart():
    product = input("Enter product name: ").lower()

    if product in products:
        cart.append(product)
        print(product, "added to cart!")
    else:
        print("Product not found.")


def view_cart():
    if len(cart) == 0:
        print("Your cart is empty.")
    else:
        print("\n===== YOUR CART =====")

        for product in cart:
            print(product, "₹", products[product])


def remove_from_cart():
    product = input("Enter product name to remove: ").lower()

    if product in cart:
        cart.remove(product)
        print(product, "removed from cart!")
    else:
        print("Product is not in your cart.")


def calculate_total():
    total = 0

    for product in cart:
        total = total + products[product]

    print("Total Amount: ₹", total)


while True:

    print("\n===== SHOPPING CART SYSTEM =====")
    print("1. View Products")
    print("2. Add Product to Cart")
    print("3. View Cart")
    print("4. Remove Product")
    print("5. Calculate Total")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_products()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        view_cart()

    elif choice == "4":
        remove_from_cart()

    elif choice == "5":
        calculate_total()

    elif choice == "6":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice!")
