import time
import random

# checks if n is evenly divisible by previous primes
def is_prime(n: int, list_primes: list) -> bool:
    for prime in list_primes:
        # an int multiple will be <= half of an int n - so if a prime is > half of n, then n is also prime
        if prime > int(n**0.5): 	
            return True
        # if n evenly divisible by a prime, it is not prime (is composite)
        if n % prime == 0:	
            return False
    return True

def get_primes_less_than_N_optimized(n: int) -> int:
      
    list_primes = [2, 3]

    # special case where user is asking for 1st or 2nd prime
    if n == 1 or n == 2:
        return list_primes[n - 1]

    next_prime = list_primes[len(list_primes) - 1]	# set next_prime to end of list_primes, which = 3
    # loop while we havent added the next prime
    while next_prime < n:
        if is_prime(next_prime, list_primes):
            list_primes.append(next_prime)
            print(str(next_prime) + '****')
        next_prime += 2
    return(next_prime)

def prompt_menu():
    game = int(input('Press a number: \n 1. Guess Number Game. \n 2. Hangman. \n 3. Print Primes. \n 4. Exit. \n'))
    result = False
    match game:
        case 1:
            # result = ask_num_game()
            result = 1
        case 2:
            # result = hangman()
            result = 2
        case 3:
            n = int(input('Enter prime number upper bound: \n'))
            result = get_primes_less_than_N_optimized(n)
        case 4:
            result = False
    return result

if __name__ == "__main__":
    # Menu Prompting
    game_over = False
    while not game_over:
        result = prompt_menu()
        if result is False:
             game_over = True
