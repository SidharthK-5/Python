"""
Program to print all lexico-graphic permutations of a string with given length
"""

from itertools import permutations

string, length = input().split()
length = int(length)

print(*["".join(item) for item in permutations(sorted(string), length)], sep="\n")
