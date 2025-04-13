import random
import os
from hangman_words import word_list
from hangman_arts import stages, logo


words = word_list

# computer chooses a random word
chosen_word = random.choice(words)
display = ['_'] * len(chosen_word)
end_of_game = False
lives = 5
hint = 3
print("Welcome to my hangman game")
print(logo)
while not end_of_game:
    # print(chosen_word)
    # get the user to guess a letter
    guess = input("Guess a letter: ").lower()
    word_length = len(chosen_word)

    if guess in display:
        print(f"psst! You've already guessed the word {guess}. Try again!")
        
    for position in range(word_length):
        # print(position)
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            
    if guess not in chosen_word:
        lives -= 1
        print(f"wrong guess, you have {lives} lives left")
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print(f"You lose. The chosed word was {chosen_word}")
    
    print(display)
    if '_' not in display:
        end_of_game = True
        print("You win")

print(f"Yay! The word is {''.join(chosen_word)}")