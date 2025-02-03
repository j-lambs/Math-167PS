MAX_STRIKES = 6
SECRET_WORD = 'MOXIE'

def make_guess_word():
    guess_word = []
    for letter in SECRET_WORD:
        guess_word.append('_')
    return guess_word

# def print_current_word(letters_remaining):
#     for letter in SECRET_WORD:
#         if 

def hangman():
    strikes = 0
    game_over = False
    guess_word = make_guess_word()
    letters_remaining = list(SECRET_WORD)

    while not game_over:
        guess_letter = input('Guess a letter! \n').upper()
        if guess_letter in letters_remaining:
            letters_remaining.remove(guess_letter)

            print(f'{guess_letter} is part of the secret word!')
            # print_current_word(letters_remaining)
            
            if len(letters_remaining) <= 0:
                game_over = True
                print('YOU WON THE GAME!')
                print(f'The secret word was {SECRET_WORD}')
        else:
            strikes += 1
            if strikes >= MAX_STRIKES:
                game_over = True
                print('Sorry, try again :(')
            print(f'Num Strikes: {strikes}')
        
    
hangman()

