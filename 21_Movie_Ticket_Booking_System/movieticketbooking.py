movies = [
    "Avengers",
    "Inception",
    "Interstellar",
    "RRR"
]

prices = [
    250,
    200,
    220,
    180
]


def show_movies():
    print("\n===== AVAILABLE MOVIES =====")

    for i in range(len(movies)):
        print(i + 1, movies[i], "- ₹", prices[i])


def book_ticket():
    show_movies()

    choice = int(input("\nEnter movie number: "))

    if choice < 1 or choice > len(movies):
        print("Invalid movie choice.")
        return

    tickets = int(input("Enter number of tickets: "))

    if tickets <= 0:
        print("Enter a valid number of tickets.")
        return

    movie_index = choice - 1

    movie_name = movies[movie_index]
    ticket_price = prices[movie_index]

    total = ticket_price * tickets

    if tickets >= 5:
        discount = total * 0.10
    elif tickets >= 3:
        discount = total * 0.05
    else:
        discount = 0

    final_amount = total - discount

    print("\n===== BOOKING SUMMARY =====")
    print("Movie:", movie_name)
    print("Ticket Price: ₹", ticket_price)
    print("Number of Tickets:", tickets)
    print("Total: ₹", total)
    print("Discount: ₹", discount)
    print("Final Amount: ₹", final_amount)


print("===== MOVIE TICKET BOOKING SYSTEM =====")

while True:

    print("\n1. View Movies")
    print("2. Book Tickets")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_movies()

    elif choice == "2":
        book_ticket()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
