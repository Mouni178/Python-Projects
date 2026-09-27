products = []
prices = []


def add_products():
    number = int(input("Enter number of products: "))

    for i in range(number):
        product = input("Enter product name: ")
        price = float(input("Enter product price: "))

        if price > 0:
            products.append(product)
            prices.append(price)
        else:
            print("Price must be greater than 0.")


def analyze_prices():
    if len(products) == 0:
        print("No products available.")
        return

    total = sum(prices)
    average = total / len(prices)
    highest = max(prices)
    lowest = min(prices)

    highest_index = prices.index(highest)
    lowest_index = prices.index(lowest)

    above_average = 0

    for price in prices:
        if price > average:
            above_average += 1

    print("\n===== PRODUCT PRICE ANALYSIS =====")

    print("Products:", products)
    print("Prices:", prices)

    print("Total Price:", total)
    print("Average Price:", round(average, 2))

    print(
        "Most Expensive:",
        products[highest_index],
        "₹",
        highest
    )

    print(
        "Cheapest:",
        products[lowest_index],
        "₹",
        lowest
    )

    print("Products Above Average:", above_average)


print("===== PRODUCT PRICE ANALYZER =====")

add_products()
analyze_prices()
