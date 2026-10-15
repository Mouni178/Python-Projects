contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

    print("Contact added successfully!")


def view_contacts():
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        print("\n===== CONTACT LIST =====")

        for i in range(len(contacts)):
            print("\nContact Number:", i + 1)
            print("Name:", contacts[i]["name"])
            print("Phone:", contacts[i]["phone"])
            print("Email:", contacts[i]["email"])


def search_contact():
    if len(contacts) == 0:
        print("No contacts available.")
        return

    search_name = input("Enter name to search: ").lower()
    found = False

    for contact in contacts:
        if search_name in contact["name"].lower():
            print("\nContact Found!")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    if len(contacts) == 0:
        print("No contacts available.")
        return

    name = input("Enter the name of the contact to update: ").lower()
    found = False

    for contact in contacts:
        if contact["name"].lower() == name:
            print("1. Update Phone Number")
            print("2. Update Email Address")

            choice = input("Enter your choice: ")

            if choice == "1":
                contact["phone"] = input("Enter new phone number: ")
                print("Phone number updated successfully!")

            elif choice == "2":
                contact["email"] = input("Enter new email address: ")
                print("Email updated successfully!")

            else:
                print("Invalid choice!")

            found = True
            break

    if not found:
        print("Contact not found.")


def delete_contact():
    if len(contacts) == 0:
        print("No contacts available.")
        return

    name = input("Enter the name of the contact to delete: ").lower()
    found = False

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            found = True
            break

    if not found:
        print("Contact not found.")


while True:
    print("\n===== CONTACT BOOK MANAGER =====")
    print("1. Add Contact")
    print("2. View Contacts")
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
        print("Thank you for using Contact Book Manager!")
        break

    else:
        print("Invalid choice. Please try again.")
