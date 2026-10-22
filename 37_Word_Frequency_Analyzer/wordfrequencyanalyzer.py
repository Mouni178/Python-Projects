
def analyze_text(text):
    words = text.lower().split()

    cleaned_words = []

    for word in words:
        word = word.strip(".,!?;:\"'()[]{}")
        if word != "":
            cleaned_words.append(word)

    if len(cleaned_words) == 0:
        print("No words found.")
        return

    unique_words = []

    for word in cleaned_words:
        if word not in unique_words:
            unique_words.append(word)

    print("\n===== WORD FREQUENCY REPORT =====")
    print("Total words:", len(cleaned_words))
    print("Unique words:", len(unique_words))
    print("\nWord Counts:")

    highest_count = 0
    most_frequent_word = ""

    for word in unique_words:
        count = cleaned_words.count(word)

        print(word, ":", count)

        if count > highest_count:
            highest_count = count
            most_frequent_word = word

    print("\nMost frequent word:", most_frequent_word)
    print("Frequency:", highest_count)


print("===== WORD FREQUENCY ANALYZER =====")

text = input("Enter a sentence or paragraph: ")

if text.strip() == "":
    print("Please enter some text.")
else:
    analyze_text(text)

