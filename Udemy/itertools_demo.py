"""
Demo on itertools library functions
"""

import itertools

# Simple iter demo - no need of itertools
lst = [10, 20, 30, 40]
iterable = iter(lst)
print("Simple iteration")
for value in iterable:
    print(value, end=" ")

# Itertools chain method
print("\n\nItertools chain method")
list1 = [100, 200, 300, 400]
list2 = [1000, 2000, 3000, 4000]
iterable = itertools.chain(
    lst, list1, list2
)  # creates an iterable by combining list2 at the end of list1
for value in iterable:
    print(value, end=" ")

# Itertools cycle - for cyclic iteration
print("\n\nItertools cycle - for cyclic iteration")
count = 0
for value in itertools.cycle(lst):
    if count < 20:
        print(value, end=" ")
    else:
        break
    count += 1

# Itertools repeat - for repeated iteration of same iterable
print("\n\nItertools repeat - for repeated iteration of same iterable")
count = 0
iterable = itertools.repeat(lst)
for value in iterable:
    if count < 5:
        print(value, end=" ")
    else:
        break
    count += 1

# Itertools tee - cycling iteration
print("\n\nItertools tee - cycling iteration")
iterable = iter(lst)
t = itertools.tee(iterable, 5)  # This will create 5 independent iterables of 'iterable'
for j in range(5):
    for value in t[j]:
        print(value, end=" ")

# Itertools islice method for slicing chain
print("\n\nItertools islice method for slicing chain")
iterable = itertools.chain(lst, list1, list2)
for value in itertools.islice(iterable, 0, 6):
    print(value, end=" ")

# count() for infinite value generation
print("\n\ncount() for infinite value generation")
count = 0
for value in itertools.count(
    10, 5
):  # We can only specify start and step, but not end. It is defined using counter
    if count > 10:
        break
    else:
        print(value, end=" ")
    count += 1

# product() will return the cartesian product of list1 and list2 as tuples
print("\n\nproduct() will return the cartesian product of list1 and list2")
prod = itertools.product(list1[:3], list2[:3])
print(f"Cartesian product of {list1[:3]} and {list2[:3]} is: \n{list(prod)}")

# Permutations and combinations
# parameters: list and no of items for combination/permutaion
lst = [1, 2, 3]
print(f"\nPermutations with 2 nums: {list(itertools.permutations(lst, 2))}")
print(f"Combinations with 2 nums: {list(itertools.combinations(lst, 2))}")
