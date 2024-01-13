import random

# random decimal value from 0-1
print(random.random())

# Random value from a list
l = [1, 2, 3, 4, 5, 6]
print(random.choice(l))

# Random integer from a range
print(random.randint(10, 100))  # from 10 to 100
print(random.randrange(10, 100))  # from 10 to 99

# Floating point random no from range
print(random.uniform(10, 20))
