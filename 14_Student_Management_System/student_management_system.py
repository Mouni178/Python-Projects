students = []


def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n===== STUDENTS =====")

    for student in students:
        print(
            "Name:", student["name"],
            "| Roll No:", student["roll_no"],
            "| Marks:", student["marks"]
        )


def search_student():
    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found")
            print("Name:", student["name"])
            print("Roll No:", student["roll_no"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def update_student():
    roll_no = input("Enter roll number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:

            print("1. Update Name")
            print("2. Update Marks")

            choice = input("Enter your choice: ")

            if choice == "1":
                student["name"] = input("Enter new name: ")
                print("Name updated successfully!")

            elif choice == "2":
                student["marks"] = float(input("Enter new marks: "))
                print("Marks updated successfully!")

            else:
                print("Invalid choice.")

            return

    print("Student not found.")


def delete_student():
    roll_no = input("Enter roll number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def calculate_average():
    if len(students) == 0:
        print("No students available.")
        return

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    print("Average Marks:", round(average, 2))


def top_student():
    if len(students) == 0:
        print("No students available.")
        return

    highest = students[0]

    for student in students:
        if student["marks"] > highest["marks"]:
            highest = student

    print("\n===== TOP STUDENT =====")
    print("Name:", highest["name"])
    print("Roll No:", highest["roll_no"])
    print("Marks:", highest["marks"])


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average Marks")
    print("7. Find Top Student")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        calculate_average()

    elif choice == "7":
        top_student()

    elif choice == "8":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
