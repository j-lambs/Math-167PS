#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:53:27 2025

@author: greglabmeier
"""
import os #for clearing the screen
os.system('clear') 

print("Welcome to hangman!")

# Converts string to a list for better searching
word_to_guess = list(input("Enter a word "))

#clear the screen to hide the word to guess
os.system('clear') 

# keep word_to_guess static, but remove correct letters from letters_left_to_guess
letters_left_to_guess = word_to_guess.copy()

# initialize current_board to all *, meaning the characters are hidden
current_board = len(word_to_guess) * ["*"]

length_of_word = len(word_to_guess)
number_of_letters_left = len(letters_left_to_guess)

# Thanks chatGPT
hangman_stages = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ---"""
]


# Thanks chatGPT creates a list of all the alphabet without me having to manually type
import string
letters_available = list(string.ascii_lowercase)
letters_used = [] 

mistakes = 0

# continue playing the game until all the letters are guess or there was 6 mistakes
while number_of_letters_left > 0 and mistakes <6:
    os.system('clear')
    print(hangman_stages[mistakes])
    print("letters available", '|'.join(letters_available) )
    print("letters used     ", '|'.join(sorted(letters_used)))
    print("current board    ",''.join(current_board))

    guess = input("give me a letter")

    # If the guess exists in the current available letters
    if guess in letters_available:
        
        
        if guess in word_to_guess:
            print("correct!")
            
            # remove letter from available letters so you don't repeat previous letters
            letters_available.remove(guess)
            letters_used.append(guess)
            dups = 0
            
            # Check if the letter shows up multiple times
            while guess in letters_left_to_guess:
                for i in range(length_of_word):
                    if letters_left_to_guess[i] == guess:
                        letters_left_to_guess[i] = '*'
                        current_board[i] = guess
            
            # After a positive find, recalculate letters left
            number_of_letters_left = 0
            for i in range(length_of_word):
                if letters_left_to_guess[i] != '*':
                    number_of_letters_left=number_of_letters_left+1
    
        else:
            print("incorrect")
            mistakes=mistakes+1
            letters_available.remove(guess)
            letters_used.append(guess)

            
    else:
        print('already used that')

        
# Debugging prints
#    print("guess",guess)
#    print("alphabet",alphabet_list)
#    print("letters left to guess",letters_left_to_guess)
    


if number_of_letters_left == 0:
    print("YOU WON!!")
else:
    print("YOU LOST")
    print("the word was",''.join(word_to_guess))
