numbers = []

def add_numbers():
    count = int(input("How many numbers do you want to enter? "))

    if count <= 0:
        print("Enter a positive count.")
        return

    for i in range(count):
        number = float(input("Enter number: "))
        numbers.append(number)

    print("Numbers added successfully!")


def analyze_numbers():
    if len(numbers) == 0:
        print("No numbers available.")
        return

    total = sum(numbers)
    average = total / len(numbers)

    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for number in numbers:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1

        if number.is_integer():
            if int(number) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    print("\n===== NUMBER ANALYSIS =====")
    print("Numbers:", numbers)
    print("Total Count:", len(numbers))
    print("Sum:", total)
    print("Average:", round(average, 2))
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Even Integers:", even_count)
    print("Odd Integers:", odd_count)
    print("Positive Numbers:", positive_count)
    print("Negative Numbers:", negative_count)
    print("Zeros:", zero_count)
    print("Unique Numbers:", unique_numbers)


while True:
    print("\n===== NUMBER STATISTICS ANALYZER =====")
    print("1. Add Numbers")
    print("2. Analyze Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_numbers()
    elif choice == "2":
        analyze_numbers()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
