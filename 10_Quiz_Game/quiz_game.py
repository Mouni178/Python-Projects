questions = [
    "What is the capital of India?",
    "Which language is used for AI and Machine Learning?",
    "What is 10 + 20?",
    "Which keyword is used to define a function in Python?",
    "Which data type stores multiple values in Python?"
]

options = [
    ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
    ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
    ["A. 20", "B. 25", "C. 30", "D. 40"],
    ["A. function", "B. define", "C. def", "D. fun"],
    ["A. int", "B. float", "C. list", "D. boolean"]
]

answers = ["B", "A", "C", "C", "C"]

score = 0

print("===== PYTHON QUIZ GAME =====")

for i in range(len(questions)):

    print("\nQuestion", i + 1)
    print(questions[i])

    for option in options[i]:
        print(option)

    user_answer = input("Enter your answer: ").upper()

    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer:", answers[i])

print("\n===== QUIZ RESULT =====")

print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Wrong Answers:", len(questions) - score)

percentage = (score / len(questions)) * 100

print("Score:", score, "/", len(questions))
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent!")

elif percentage >= 60:
    print("Good job!")

elif percentage >= 40:
    print("Keep practicing!")

else:
    print("You need more practice.")
