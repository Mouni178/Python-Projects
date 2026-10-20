player_score = 0
computer_score = 0
draws = 0

print("===== ROCK PAPER SCISSORS =====")

while True:
    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice.")
        continue

    if choice == "1":
        player = "rock"
    elif choice == "2":
        player = "paper"
    else:
        player = "scissors"

    # Generate the computer's move without importing anything.
    computer_number = (player_score + computer_score + draws) % 3 + 1

    # Rotate the computer's move for the next round.
    computer = ["rock", "paper", "scissors"][computer_number - 1]

    print("Your move:", player)
    print("Computer move:", computer)

    if player == computer:
        print("It's a draw!")
        draws += 1

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        player_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print("\n===== SCOREBOARD =====")
    print("Your Score:", player_score)
    print("Computer Score:", computer_score)
    print("Draws:", draws)

print("\n===== FINAL RESULT =====")
print("Your Score:", player_score)
print("Computer Score:", computer_score)
print("Draws:", draws)

if player_score > computer_score:
    print("Congratulations! You won overall.")
elif computer_score > player_score:
    print("Computer won overall.")
else:
    print("The game ended in a tie.")
