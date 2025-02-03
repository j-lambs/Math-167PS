import time

def get_primes_less_than_N_all_numbers(n: int) -> int:
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
		else:
			print(next_prime)
		next_prime += 1

def get_primes_less_than_N_primes_only(n: int) -> int:
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


# checks if n is evenly divisible by previous primes
def is_prime(n: int, list_primes: list) -> bool:
	n_sqrt = int(n**0.5)
	for prime in list_primes:
		if prime > n_sqrt: 	# an int multiple will be <= half of an int n - so if a prime is > half of n, then n is also prime
			return True
		if n % prime == 0:	# if n evenly divisible by a prime, it is not prime (is composite)
			return False
	return True

if __name__ == "__main__":
    n = int(input('Enter prime number upper bound: \n'))

    start_all = time.time()
    print(get_primes_less_than_N_all_numbers(n))
    end_all = time.time()
    
    start_primes = time.time()
    print(get_primes_less_than_N_primes_only(n))
    end_primes = time.time()
	
    print(f'All Numbers Time: {end_all - start_all}')
    print(f'Primes Only Time: {end_primes - start_primes}')
