# Q12: Number Guessing Game - WHILE loop: runs until the guess is correct
# Generate a random number between 1–100. Keep asking the user to guess until they find the correct number. 
# After each incorrect guess, display "Too High" or "Too Low". 
# Finally display the number of attempts taken.

import random

secret = random.randint(1, 100)
attempts = 0
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")
    else:
        print(f"Correct! You took {attempts} attempts.")
        break
