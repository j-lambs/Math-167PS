import random
import math
MAX_NUM = 100

def make_population():
    population = []
    for i in range(1, MAX_NUM + 1):
        population.append(i)
    return population

population = make_population()
sample_size = MAX_NUM
sampled_elements = random.sample(population, sample_size)

# main
cur_max = 0
counter = 0
# draw first N/e random sample
while counter < math.floor(MAX_NUM / math.e):
    if sampled_elements[counter] > cur_max:
        cur_max = sampled_elements[counter]
    counter += 1
print(f'{MAX_NUM}/e Max = {cur_max}')

# draw until > max(random sample)
next_biggest = 0
while counter < MAX_NUM or next_biggest < cur_max:
    if sampled_elements[counter] > cur_max:
        next_biggest = sampled_elements[counter]
    counter += 1

print(f'Max after {MAX_NUM}/e draws: {next_biggest}')
