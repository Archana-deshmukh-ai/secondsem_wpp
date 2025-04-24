import random

random_integers = [random.choice([0, 1]) for _ in range(100)]
max_zeros = 0
current_zeros = 0

for num in random_integers:
    if num == 0:
        current_zeros += 1
    else:
        max_zeros = max(max_zeros, current_zeros)
        current_zeros = 0

print(max_zeros)
