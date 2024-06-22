"""
Program to print all lexico-graphic combinations of a string upto given length
"""

from itertools import combinations

string, length = input().split()
length = int(length)

for size in range(1, length + 1):
    print(*["".join(item) for item in combinations(sorted(string), size)], sep="\n")
