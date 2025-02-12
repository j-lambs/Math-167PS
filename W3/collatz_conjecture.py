
def find_collatz_seq(n):
	counter = 0
	peak = n
	while n != 1:
		print(n)
		if n % 2 == 0:
			n = int(n / 2)
		else:
			n = 3 * n + 1
		counter += 1
		
		if n > peak:
			peak = n
	print(f'Peak of Mountain: {peak}')
	return counter

n = 10
print(f'Collatz Length of {n}: {find_collatz_seq(n)}')
