
names = []
maths_marks = []
python_marks = []
english_marks = []


def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    for existing_name in names:
        if existing_name.lower() == name.lower():
            print("Student already exists.")
            return

    maths = float(input("Enter Maths marks (0-100): "))
    python = float(input("Enter Python marks (0-100): "))
    english = float(input("Enter English marks (0-100): "))

    if not (0 <= maths <= 100 and
            0 <= python <= 100 and
            0 <= english <= 100):
        print("Marks must be between 0 and 100.")
        return

    names.append(name)
    maths_marks.append(maths)
    python_marks.append(python)
    english_marks.append(english)

    print("Student result added successfully!")


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def show_result(index):
    total = (
        maths_marks[index]
        + python_marks[index]
        + english_marks[index]
    )

    average = total / 3
    grade = calculate_grade(average)

    print("\nStudent Name:", names[index])
    print("Maths:", maths_marks[index])
    print("Python:", python_marks[index])
    print("English:", english_marks[index])
    print("Total:", total, "/ 300")
    print("Average:", round(average, 2))
    print("Grade:", grade)

    if min(
        maths_marks[index],
        python_marks[index],
        english_marks[index]
    ) >= 35:
        print("Result: PASS")
    else:
        print("Result: FAIL")


def view_all_results():
    if len(names) == 0:
        print("No student records available.")
        return

    for i in range(len(names)):
        print("\n===== RESULT", i + 1, "=====")
        show_result(i)


def find_topper():
    if len(names) == 0:
        print("No student records available.")
        return

    topper_index = 0

    for i in range(1, len(names)):
        current_total = (
            maths_marks[i] + python_marks[i] + english_marks[i]
        )

        topper_total = (
            maths_marks[topper_index]
            + python_marks[topper_index]
            + english_marks[topper_index]
        )

        if current_total > topper_total:
            topper_index = i

    print("\n===== CLASS TOPPER =====")
    show_result(topper_index)


def search_student():
    search_name = input("Enter student name to search: ").strip()

    for i in range(len(names)):
        if names[i].lower() == search_name.lower():
            show_result(i)
            return

    print("Student not found.")


while True:
    print("\n===== EXAM RESULT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View All Results")
    print("3. Find Class Topper")
    print("4. Search Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all_results()
    elif choice == "3":
        find_topper()
    elif choice == "4":
        search_student()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
      
