rooms = [101, 102, 103, 104, 105]

booked_rooms = []
customer_names = []
number_of_days = []

room_price = 1500


def view_rooms():
    print("\n===== AVAILABLE ROOMS =====")

    if len(rooms) == 0:
        print("No rooms available.")
    else:
        for room in rooms:
            print("Room", room, "- ₹", room_price, "per day")


def book_room():
    if len(rooms) == 0:
        print("No rooms available.")
        return

    view_rooms()

    room = int(input("Enter room number: "))

    if room not in rooms:
        print("Invalid or unavailable room.")
        return

    name = input("Enter customer name: ")
    days = int(input("Enter number of days: "))

    if days <= 0:
        print("Enter a valid number of days.")
        return

    rooms.remove(room)
    booked_rooms.append(room)
    customer_names.append(name)
    number_of_days.append(days)

    total = room_price * days

    print("\nRoom booked successfully!")
    print("Customer:", name)
    print("Room:", room)
    print("Days:", days)
    print("Total Cost: ₹", total)


def view_bookings():
    if len(booked_rooms) == 0:
        print("No bookings found.")
    else:
        print("\n===== BOOKINGS =====")

        for i in range(len(booked_rooms)):
            total = room_price * number_of_days[i]

            print(
                i + 1,
                customer_names[i],
                "- Room",
                booked_rooms[i],
                "-",
                number_of_days[i],
                "days - ₹",
                total
            )


def cancel_booking():
    if len(booked_rooms) == 0:
        print("No bookings found.")
        return

    view_bookings()

    room = int(input("\nEnter room number to cancel: "))

    if room in booked_rooms:

        index = booked_rooms.index(room)

        booked_rooms.pop(index)
        customer_names.pop(index)
        number_of_days.pop(index)

        rooms.append(room)

        print("Booking cancelled successfully.")

    else:
        print("Booking not found.")


while True:

    print("\n===== HOTEL BOOKING SYSTEM =====")
    print("1. View Available Rooms")
    print("2. Book Room")
    print("3. View Bookings")
    print("4. Cancel Booking")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_rooms()

    elif choice == "2":
        book_room()

    elif choice == "3":
        view_bookings()

    elif choice == "4":
        cancel_booking()

    elif choice == "5":
        print("Thank you for using Hotel Booking System.")
        break

    else:
        print("Invalid choice.")
