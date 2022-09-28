# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
lives = 10
if difficulty == "hard":
    lives = 5
count = 0
computer_choice = random.randint(1, 100)
ending = f"You lose. Computer choice was: {computer_choice}."
while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == computer_choice:
        ending = f"You win! Computer choice was: {computer_choice}. It takes only {count} attempts."
        lives = 0
    elif guess > computer_choice:
        print("Too high.\nGuess again.")
        lives -= 1
        count += 1
    else:
        print("Too low.\nGuess again.")
        lives -= 1
        count += 1


print(ending)
