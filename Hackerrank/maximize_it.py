"""
Question:
Given K no of lists and an integer M
Take exactly one element from each list, not necessarily the largest element.
Add the squares of the chosen elements and perform the modulo operation with M.
The maximum modulo value obtained is the answer to the problem
"""

from itertools import product


K, M = map(int, input().split())
lists = []

for _ in range(K):
    row = list(map(int, input().split()))
    # Skipping the 1st entry in the line because it only denotes the no. of elements in that list
    lists.append(row[1:])

# product(list[list]) will return a list of tuple, where each will be a permutation of one element per inner lists
products = product(*lists)

"""
Make a list of mod of sum of products
Take each tuple, find the sum of squares of elements in it. Add these sums to mods list
Get the max value from mods
"""
mods = [sum(map(lambda item: pow(item, 2), tupl)) % M for tupl in products]

# Get the maximum value of modulo
print(max(mods))
