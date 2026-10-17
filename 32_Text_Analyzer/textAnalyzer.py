def analyze_text(text):
    words = text.split()

    print("\n===== TEXT ANALYSIS =====")
    print("Total Characters:", len(text))
    print("Characters Without Spaces:", len(text.replace(" ", "")))
    print("Total Words:", len(words))
    print("Total Sentences:", sum(text.count(mark) for mark in ".!?"))

    if len(words) > 0:
        longest = max(words, key=len)
        print("Longest Word:", longest)

    vowels = 0
    consonants = 0

    for character in text.lower():
        if character in "aeiou":
            vowels += 1
        elif character.isalpha():
            consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)


def search_word(text):
    word = input("Enter word to search: ").strip()

    if word == "":
        print("Word cannot be empty.")
        return

    count = text.lower().split().count(word.lower())

    print("Word occurrences:", count)


print("===== TEXT ANALYZER =====")

text = input("Enter a sentence or paragraph: ")

if text.strip() == "":
    print("Please enter some text.")
else:
    analyze_text(text)

    while True:
        print("\n1. Search for a Word")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_word(text)
        elif choice == "2":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")
