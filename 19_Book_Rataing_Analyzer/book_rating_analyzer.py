books = []
ratings = []


def add_books():
    number = int(input("Enter number of books: "))

    for i in range(number):
        book = input("Enter book name: ")
        rating = float(input("Enter rating (1-5): "))

        if rating >= 1 and rating <= 5:
            books.append(book)
            ratings.append(rating)
        else:
            print("Rating must be between 1 and 5.")


def analyze_ratings():
    if len(books) == 0:
        print("No books available.")
        return

    total = sum(ratings)
    average = total / len(ratings)

    highest = max(ratings)
    lowest = min(ratings)

    highest_index = ratings.index(highest)
    lowest_index = ratings.index(lowest)

    good_books = 0

    for rating in ratings:
        if rating >= 4:
            good_books += 1

    print("BOOK RATING ANALYSIS")

    print("\nBooks and Ratings:")

    for i in range(len(books)):
        print(books[i], "-", ratings[i], "/ 5")

    print("\nAverage Rating:", round(average, 2))
    print(
        "Highest Rated Book:",
        books[highest_index],
        "-", highest
    )
    print(
        "Lowest Rated Book:",
        books[lowest_index],
        "-", lowest
    )
    print("Books Rated 4 or Above:", good_books)


print("BOOK RATING ANALYZER")

add_books()
analyze_ratings()
