import random
from hangman_aux import *
max_lives = 6



chosen_word = random.choice(word_list)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []

for i in range(len(chosen_word)):
    display.append("_")


# Main game is inside the while loop
end = 0 # Flag that controls when the game should end
lives = max_lives # Create a variable lives to control how many miss attempts the user has left
print(stages[-1]) 
while end == 0:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)): # Substitute "_" by the guessed letter when appropriate
        if guess == chosen_word[i]:
            display[i] = guess
    if guess not in chosen_word: # If the guess was wrong, the number of lives is subtracted by one
        lives -= 1
        print(stages[lives])
        if lives == 0: # If there are no more lives, the loop breaks and it is Game Over
            print("Game Over")
            print(f"The word was {chosen_word}")
            break
    print(display)
    if "_" not in display:
        print("You win")
        end = 1

