import random
import os
from hangman_words import word_list
from hangman_arts import stages, logo


words = word_list

# computer chooses a random word
chosen_word = random.choice(words)
display = ["-"] * len(chosen_word)
lives = 5
print("Hello and welcome to my hangman game!")
print(hangman_logo)
end_of_game = False
while not end_of_game:
    guess = input("I have chosen a word, can you guess a letter in the word? \n").lower()
    word_length = len(chosen_word)
    if guess in display:
        print(f"You have guessed the letter before. Try again")
        
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    if guess not in chosen_word:
        lives -= 1
        print(f"wrong guess. You have {lives} lives left")
        print(hangman_stages[lives])
        hint = input("Would you like to get an hint? (yes/no): ")
        
        if hint.lower() == "yes":
            position = random.randint(0, len(chosen_word) - 1)
            hint_letter = chosen_word[position]
            display[position] = hint_letter
        #print(display)
        
        if lives == 0:
            end_of_game = True
            print(f"You lose. The chosen word was {chosen_word}")
            
    print(display)
    if "-" not in display:
        end_of_game = True
        print("You won")
        
print(f"Yay, the word is {"".join(display)}")