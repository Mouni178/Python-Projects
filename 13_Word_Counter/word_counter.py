text = input("Enter a sentence: ")
words = text.split()
word_count = len(words)
characters = len(text)
print("TEXT ANALYSIS")
print("Total words:", word_count)
print("Total characters:", characters)
frequency = {}
for word in words:
    word = word.lower()
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("WORD FREQUENCY")
for word, count in frequency.items():
    print(word, ":", count)
