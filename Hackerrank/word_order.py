"""
Given N words. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
"""

from collections import Counter

N = int(input())
A = []
for i in range(N):
    r = input()
    A.append(r)

# Count the occurrences of each word and save it in a dictionary
# The dictionary will have the word as key and the count as value
dict = dict(Counter(A))

print(len(dict))
print(*dict.values())
