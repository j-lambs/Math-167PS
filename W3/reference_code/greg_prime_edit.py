#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 19:43:00 2025

@author: greglabmeier
"""
import time

def prime_nums_slow():
    n = 50000
    start = time.time() # Get current timestamp

    for number_to_test in range(3, n):
        is_a_prime = True

        for current_divide_by in range(3,int(number_to_test)+1,2):
            if number_to_test % current_divide_by == 0:
                is_a_prime = False
    
    end = time.time()
    print("Total Time Non-Optimized for up to 50000:", end - start)
    return end - start

def prime_nums_optimized():
    n = 50000
    start = time.time() # Get current timestamp

    for number_to_test in range(3, n ,2):
        is_a_prime = True

        for current_divide_by in range(3,int(number_to_test**0.5)+1,2):
            if number_to_test % current_divide_by == 0:
                is_a_prime = False
    
    end = time.time()
    print("Total Time Optimized for up to 50000:", end - start)
    return end - start

def get_Nth_prime(n: int) -> int:
    list_primes = [2, 3]

    # special case where user is asking for 1st or 2nd prime
    if n == 1 or n == 2:
        return list_primes[n - 1]

    next_prime = list_primes[len(list_primes) - 1]	# set next_prime to end of list_primes, which = 3
    # loop while we havent added the next prime
    while len(list_primes) != n:
        next_prime += 2
        if is_prime(next_prime, list_primes):
            list_primes.append(next_prime)
    # print(list_primes)
    print(f'{n}th Prime = {next_prime}')
    return next_prime

# checks if n is evenly divisible by previous primes
def is_prime(n: int, list_primes: list) -> bool:
    n_sqrt = int(n**0.5)
    for prime in list_primes:
        if prime > n_sqrt: 	# an int multiple will be <= half of an int n - so if a prime is > half of n, then n is also prime
            return True
        if n % prime == 0:	# if n evenly divisible by a prime, it is not prime (is composite)
            return False
    return True

prime_time_slow = prime_nums_slow()
prime_time_fast = prime_nums_optimized()
print(f'Time saved through optimization with n = 50000: {prime_time_slow - prime_time_fast}')
# Total Time Non-Optimized for up to 50000: 24.352458000183105
# Total Time Optimized for up to 50000: 0.05708479881286621
# Time saved through optimization with n = 50000: 24.29537320137024

N = 2000000
start = time.time()
get_Nth_prime(N)
end = time.time()
print(f'Time to get {N}th prime: {end - start}')
# 2000000th Prime = 32,452,843
# Time to get 2000000th prime: 60.06425404548645

