import random

def secret_num_dist_comparison(dist_new, dist_old):
    if dist_new > dist_old:
        print('Colder.')
    else:
        print('WARMER!')

def ask_num_game():
    low = 1
    high = 100
    secret_num = random.randint(low, high) # generate random secret number
    num_guess = 0
    temp_dist_to_secret_num = 100
    max_guess = secret_num
    min_guess = secret_num
    game_over = False
    

    while not game_over:
        guess = int(input(f'Input a number between {low} and {high} \n'))

        # Give warnings if player guess larger than max_guess
        # or guess smaller than min_guess
        if num_guess != 0:
            if guess > max_guess and guess > secret_num:
                print('WARNING: Bigger guess than before.')
            else:
                max_guess = guess
            if guess < min_guess and guess < secret_num:
                print('WARNING: Smaller guess than before.')
            else:
                min_guess = guess

        dist_to_secret_num = abs(secret_num - guess)
        
        if guess == secret_num:
            game_over = True
        elif guess < secret_num:
            # Tell player how close they are (low)
            if dist_to_secret_num >= 30 and dist_to_secret_num < 15:
                print('Wayyy too low')
            elif dist_to_secret_num >= 15 and dist_to_secret_num < 30:
                print('Too low')
            else:
                print('Too low but close')
            
            if num_guess != 0:
                secret_num_dist_comparison(dist_to_secret_num, temp_dist_to_secret_num)
            num_guess += 1
        else:
            # Tell player how close they are (high)
            if dist_to_secret_num >= 30 and dist_to_secret_num < 15:
                print('Wayyy too high')
            elif dist_to_secret_num >= 15 and dist_to_secret_num < 30:
                print('Too high')
            else:
                print('Too high but close')

            if num_guess != 0:
                secret_num_dist_comparison(dist_to_secret_num, temp_dist_to_secret_num)
            num_guess += 1

        temp_dist_to_secret_num = dist_to_secret_num
    print('CONGRATULATIONS!!!')
    print(f'Number of guess to win: {num_guess}')

ask_num_game()
