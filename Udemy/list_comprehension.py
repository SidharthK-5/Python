"""
Various ways to do list comprehension
"""

sample_list = [10, 15, 20, 25, 30, 35]
print(f"{sample_list=}")

# Square list
list_1 = [i * i for i in sample_list]
print(f"\nsample_list_squared={list_1}")

# Even no list
list_1 = [i for i in sample_list if i % 2 == 0]
print(f"\neven nos in {sample_list}\n{list_1}")

# Length of item list
sample_list = ["abc", "abcd", "abcabc"]
list_1 = [len(i) for i in sample_list]
print(f"\nList having length of elements in {sample_list}\n{list_1}")

# Nested for loops in comprehension
sample_list = [(i, j) for i in range(1, 5) for j in range(100, 102)]
print(f"\nTuple list using nested for loops: {sample_list}")

sample_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_1 = [j for i in sample_list for j in i]
print(f"\nCreating 1D list from the 2D list {sample_list}\n{list_1}")

# Multiple output specification
sample_list = [10, 15, 20, 25, 30, 35]
list_1 = ["Even" if i % 2 == 0 else "Odd" for i in sample_list]
print(f"\nSeeing even/odd correspondance from {sample_list}\n{list_1}")

print("\nCombining two lists by taking values of same index")
int_list = [1, 2, 3, 4]
character_list = ["a", "b", "c", "d"]
new_list = [
    [i, j]
    for i in int_list
    for j in character_list
    if int_list.index(i) == character_list.index(j)
]
print(
    f"Combining values of same index from {int_list} and {character_list}\n{new_list}"
)

# Creates tuples by combining elements from a and b
print(f"Same but list of tuples: {list(zip(int_list, character_list))}")
list_2 = [list(i) for i in zip(int_list, character_list)]
print(f"As list of lists: {list_2}")

print("\nComprehension based on type of element")
alnum_list = ["P", 5, 1, "Q", "r", "6"]
string_list = [i for i in alnum_list if isinstance(i, str)]
print(f"Taking only string elements from {alnum_list}\n{string_list}")

print("\nList comprehension to create generator object")
"""
Instead of [] in comprehension, put ()
Generator object doesn't create new list, but it generates an iterable object
This saves memory space with the same utility
"""
multiples_of_5 = (i for i in range(1, 101) if i % 5 == 0)
print(f"Generator object {multiples_of_5=}")
print(f"Actual list from generator object: {list(multiples_of_5)}")
