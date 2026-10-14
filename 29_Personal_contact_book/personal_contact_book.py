contacts = {}


def add_contact():
    name = input("Enter contact name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    if name.lower() in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts[name.lower()] = {
        "name": name,
        "phone": phone,
        "email": email
    }

    print("Contact added successfully!")


def view_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
        return

    print("\n===== SAVED CONTACTS =====")

    for contact in contacts.values():
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("--------------------------")


def search_contact():
    name = input("Enter name to search: ").strip().lower()

    if name in contacts:
        contact = contacts[name]

        print("\n===== CONTACT FOUND =====")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter contact name to update: ").strip().lower()

    if name not in contacts:
        print("Contact not found.")
        return

    print("1. Update phone number")
    print("2. Update email address")

    choice = input("Enter your choice: ")

    if choice == "1":
        phone = input("Enter new phone number: ").strip()
        contacts[name]["phone"] = phone
        print("Phone number updated successfully!")

    elif choice == "2":
        email = input("Enter new email address: ").strip()
        contacts[name]["email"] = email
        print("Email updated successfully!")

    else:
        print("Invalid choice.")


def delete_contact():
    name = input("Enter contact name to delete: ").strip().lower()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


while True:
    print("\n===== PERSONAL CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Please try again.")
