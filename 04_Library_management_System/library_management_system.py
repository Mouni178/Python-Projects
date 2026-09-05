books = []
borrowed_books = []
def add_book():
    book = input("Enter book name: ")
    books.append(book)
    print("Book added successfully!")
def view_books():
    if len(books) == 0:
        print("No books available.")
    else:
        print("Available Books")
        for i in range(len(books)):
            print(i + 1, books[i])
def search_book():
    search = input("Enter book name to search: ")
    found = False
    for book in books:
        if book.lower() == search.lower():
            print("Book found:", book)
            found = True
            break
    if found == False:
        print("Book not found.")
def borrow_book():
    book = input("Enter book name to borrow: ")
    if book in books:
        books.remove(book)
        borrowed_books.append(book)
        print("Book borrowed successfully!")
    else:
        print("Book is not available.")
def return_book():
    book = input("Enter book name to return: ")
    if book in borrowed_books:
        borrowed_books.remove(book)
        books.append(book)
        print("Book returned successfully!")
    else:
        print("This book was not borrowed.")
while True:
    print("LIBRARY MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        borrow_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        print("Thank you for using Library Management System!")
        break
    else:
        print("Invalid choice. Please try again.")
