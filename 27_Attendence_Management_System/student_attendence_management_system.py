students = {}
def add_student():
    roll_no = input("Enter student roll number: ")

    if roll_no in students:
        print("Student already exists.")
        return

    name = input("Enter student name: ")
    students[roll_no] = {
        "name": name,
        "present": 0,
        "absent": 0
    }

    print("Student added successfully!")


def mark_attendance():
    if len(students) == 0:
        print("No students available.")
        return

    roll_no = input("Enter student roll number: ")

    if roll_no not in students:
        print("Student not found.")
        return

    status = input("Enter attendance (P for Present, A for Absent): ").upper()

    if status == "P":
        students[roll_no]["present"] += 1
        print("Marked as Present.")
    elif status == "A":
        students[roll_no]["absent"] += 1
        print("Marked as Absent.")
    else:
        print("Invalid attendance status.")


def view_students():
    if len(students) == 0:
        print("No students available.")
        return

    print("\n===== STUDENT ATTENDANCE =====")

    for roll_no, details in students.items():
        print("Roll Number:", roll_no)
        print("Name:", details["name"])
        print("Present:", details["present"])
        print("Absent:", details["absent"])
        print("-----------------------------")


def calculate_percentage():
    roll_no = input("Enter student roll number: ")

    if roll_no not in students:
        print("Student not found.")
        return

    present = students[roll_no]["present"]
    absent = students[roll_no]["absent"]
    total_days = present + absent

    if total_days == 0:
        print("No attendance recorded yet.")
        return

    percentage = (present / total_days) * 100

    print("\n===== ATTENDANCE REPORT =====")
    print("Student Name:", students[roll_no]["name"])
    print("Total Classes:", total_days)
    print("Classes Attended:", present)
    print("Classes Missed:", absent)
    print("Attendance Percentage:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Attendance Status: Sufficient")
    else:
        print("Attendance Status: Below 75%")


while True:
    print("\n===== STUDENT ATTENDANCE SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View All Students")
    print("4. Calculate Attendance Percentage")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_students()
    elif choice == "4":
        calculate_percentage()
    elif choice == "5":
        print("Thank you for using the Attendance System!")
        break
    else:
        print("Invalid choice. Please try again.")
