from datetime import datetime
import os

FILE_NAME = "diary.txt"


def write_entry():
    date = datetime.now().strftime("%Y-%m-%d")
    entry = input("Write your diary entry: ").strip()

    if not entry:
        print("Diary entry cannot be empty.")
        return

    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"\nDate: {date}\n")
        file.write(f"Entry: {entry}\n")
        file.write("-" * 40 + "\n")

    print("Diary entry saved successfully!")


def view_entries():
    if not os.path.exists(FILE_NAME):
        print("No diary entries found.")
        return

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        content = file.read()

    if content.strip():
        print("\n===== MY DIARY =====")
        print(content)
    else:
        print("Your diary is empty.")


def search_entry():
    if not os.path.exists(FILE_NAME):
        print("No diary entries found.")
        return

    search_date = input("Enter date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(search_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        entries = file.read().split("-" * 40)

    found = False

    for entry in entries:
        if f"Date: {search_date}" in entry:
            print("\n===== MATCHING ENTRY =====")
            print(entry.strip())
            found = True

    if not found:
        print("No entry found for this date.")


while True:
    print("\n===== PERSONAL DIARY =====")
    print("1. Write Diary Entry")
    print("2. View All Entries")
    print("3. Search Entries by Date")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        write_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        search_entry()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
