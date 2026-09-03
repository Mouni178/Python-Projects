import random
print("Number Guessing Game")
print("I have selected number from 1 to 100")
number=random.randint(1,100)
attempts=0
while True:
  guess=int(input("Enter a number:"))
  attempts+=1
  if guess<number:
    print("Too Low! Try Again")
  elif guess>number:
    print("Too High! Try Again")
  else:
    print("Correct")
    print("You guessed the number in",attempts,"attempts")
    break
  
