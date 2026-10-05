cars = ["BMW", "Audi", "Toyota", "Honda", "Hyundai"]

prices = [3000, 2500, 1500, 1200, 1000]

rented_cars = []
customer_names = []
rental_days = []


def view_cars():
    print("\n===== AVAILABLE CARS =====")

    if len(cars) == 0:
        print("No cars available.")
    else:
        for i in range(len(cars)):
            print(
                i + 1,
                cars[i],
                "- ₹",
                prices[i],
                "per day"
            )


def rent_car():
    if len(cars) == 0:
        print("No cars available.")
        return

    view_cars()

    choice = int(input("Enter car number: "))

    if choice < 1 or choice > len(cars):
        print("Invalid car number.")
        return

    customer = input("Enter customer name: ")
    days = int(input("Enter number of rental days: "))

    if days <= 0:
        print("Enter a valid number of days.")
        return

    index = choice - 1

    car = cars[index]
    price = prices[index]

    total = price * days

    rented_cars.append(car)
    customer_names.append(customer)
    rental_days.append(days)

    cars.pop(index)
    prices.pop(index)

    print("\nCar rented successfully!")
    print("Customer:", customer)
    print("Car:", car)
    print("Days:", days)
    print("Total Cost: ₹", total)


def return_car():
    if len(rented_cars) == 0:
        print("No rented cars.")
        return

    print("\n===== RENTED CARS =====")

    for i in range(len(rented_cars)):
        print(
            i + 1,
            rented_cars[i],
            "-",
            customer_names[i]
        )

    choice = int(input("Enter car number to return: "))

    if choice < 1 or choice > len(rented_cars):
        print("Invalid choice.")
        return

    index = choice - 1

    car = rented_cars[index]

    rented_cars.pop(index)
    customer_names.pop(index)
    rental_days.pop(index)

    cars.append(car)

    if car == "BMW":
        prices.append(3000)
    elif car == "Audi":
        prices.append(2500)
    elif car == "Toyota":
        prices.append(1500)
    elif car == "Honda":
        prices.append(1200)
    elif car == "Hyundai":
        prices.append(1000)

    print("Car returned successfully!")


def view_rentals():
    if len(rented_cars) == 0:
        print("No rental records found.")
        return

    print("\n===== RENTAL DETAILS =====")

    for i in range(len(rented_cars)):

        if rented_cars[i] == "BMW":
            price = 3000
        elif rented_cars[i] == "Audi":
            price = 2500
        elif rented_cars[i] == "Toyota":
            price = 1500
        elif rented_cars[i] == "Honda":
            price = 1200
        else:
            price = 1000

        total = price * rental_days[i]

        print(
            "Customer:", customer_names[i],
            "| Car:", rented_cars[i],
            "| Days:", rental_days[i],
            "| Cost: ₹", total
        )


while True:

    print("\n===== CAR RENTAL SYSTEM =====")
    print("1. View Available Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. View Rentals")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_cars()

    elif choice == "2":
        rent_car()

    elif choice == "3":
        return_car()

    elif choice == "4":
        view_rentals()

    elif choice == "5":
        print("Thank you for using Car Rental System.")
        break

    else:
        print("Invalid choice.")
