import random

random_numbers = [random.randint(1, 100) for _ in range(10)]
print("Random numbers:", random_numbers)

# Sort the list of random numbers
sorted_numbers = sorted(random_numbers)
print("Sorted numbers:", sorted_numbers)