import random

def secret_num_dist_comparison(dist_new, dist_old):
    if dist_new > dist_old:
        print('Colder.')
    else:
        print('WARMER!')

def ask_num_game():
    low = 1
    high = 100
    secret_num = random.randint(low, high)
    temp_dist_to_secret_num = 100
    game_over = False
    while not game_over:
        guess = int(input(f'Input a number between {low} and {high} \n'))
        dist_to_secret_num = abs(secret_num - guess)
        if guess == secret_num:
            game_over = True
        elif guess < secret_num:
            secret_num_dist_comparison(dist_to_secret_num, temp_dist_to_secret_num)
            print('Too low')
        else:
            secret_num_dist_comparison(dist_to_secret_num, temp_dist_to_secret_num)
            print('Too high')
        temp_dist_to_secret_num = dist_to_secret_num
    print('CONGRATULATIONS!!!')

ask_num_game()
