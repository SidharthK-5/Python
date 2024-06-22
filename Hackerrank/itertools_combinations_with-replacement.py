"""
Program to print all lexico-graphic combinations with replacement
of a string upto given length
"""

from itertools import combinations_with_replacement

string, length = input().split()
length = int(length)

print(
    *["".join(item) for item in combinations_with_replacement(sorted(string), length)],
    sep="\n"
)
