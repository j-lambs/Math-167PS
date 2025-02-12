#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:32:26 2025

@author: greglabmeier
"""
import random

# initialize valid number as False until an integer is given
valid_number = False

number_to_guess = int(random.randint(1, 100))

number_of_guesses = 1

current_guess = int(input('Please enter a guess between 1 and 100 (Enter 0 to give up)'))

# Keep asking for another number until player gets it or enters 0        
while (number_to_guess!=current_guess) and current_guess != 0:
    if number_to_guess<current_guess:
        print("Guess #:",number_of_guesses," That is too high. Try again")
    else:
        print("Guess #:",number_of_guesses," That is too low. Try again")
    
    current_guess = int(input('Please enter a guess (Enter 0 to give up): '))
    number_of_guesses = number_of_guesses + 1

# Summarize what happened in the game. Write a snarky comment if they quit
if current_guess == 0:
    print("Quitter! You gave up after",number_of_guesses,"guesses")
    print("the number was:",number_to_guess)
else:
    # It is pretty ugly to have to subtract 1 from the number of guesses...WHY?
    print("You got it! The answer was :",number_to_guess, "took you", number_of_guesses-1," guesses")
