import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = ["_" for letter in chosen_word]

print(logo)
print(stages[-1])

while lives > 0 and "_" in display:
    print(' '.join(display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        print(stages[lives])
        print(f"There isn't letter {guess} in the word.")

if lives > 0:
    print("You win!")
else:
    print(f"The word was {chosen_word}")
    print("You lose!")
