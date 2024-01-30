"""
Demo of some common functions in random module
"""

import random

# random decimal value from 0-1
print(f"Get a random decimal between 0 & 1: {random.random()}")

# Random value from a list
sample_list = [1, 2, 3, 4, 5, 6]
print(f"\nChoose a random value from {sample_list}: {random.choice(sample_list)}")

# Random integer from a range
print(f"\nRandom value in [10, 100]: {random.randint(10, 100)}")  # from 10 to 100
print(f"Random value in [10,100): {random.randrange(10, 100)}")  # from 10 to 99

# Floating point random no from range
print(f"\nGet a random decimal between 10 & 20: {random.uniform(10, 20)}")
