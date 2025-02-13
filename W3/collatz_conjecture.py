import math

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def find_collatz_seq(n):
	collatz_len = 0
	peak = n
	while not is_power_of_two(n):
		if n % 2 == 0:
			n = int(n / 2)
		else:
			n = 3 * n + 1
		collatz_len += 1
		
		if n > peak:
			peak = n
	collatz_len += int(math.log(n, 2))
	# print(f'Hailstone: {peak}') # Peak of Mountain
	return (peak, collatz_len)


if __name__ == "__main__":
	MAX_SEED = 100000
	max_hailstone = 0
	largest_relative_hailstone = 0
	for i in range(1, MAX_SEED + 1):
		#TODO: % computed printing
		# if MAX_SEED % i >= 0 and MAX_SEED % i <= 100 and MAX_SEED % 10 == 0:
		# 	print(i)
		# 	print(f'{MAX_SEED % i}% Computed...')

		collatz_info = find_collatz_seq(i)
		if collatz_info[0] > max_hailstone:
			max_hailstone = collatz_info[0]
			largest_relative_hailstone = i
		# print(f'Collatz Length of {i}: {collatz_info[1]}')

	print(f'Seed that produces largest hailstone: {largest_relative_hailstone}')
	print(f'Largest Hailstone: {max_hailstone}')
