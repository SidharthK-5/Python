"""
Given a string S, compress the string by replacing consecutive repeating characters
with tuple (Character count, character).
"""

from itertools import groupby

string = input()
groups = groupby(string)

print(*[(len(list(group)), int(key)) for key, group in groups])
