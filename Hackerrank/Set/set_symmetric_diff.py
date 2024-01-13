"""
Example of set symmetric difference operation
Symmetric difference results in a set which have non-common elements in both sets (union-intersection)
"""

# Read two sets from input
n = int(input())
english_set = set(map(int, input().split()))
b = int(input())
french_set = set(map(int, input().split()))

# Length of english set after symmetric difference
print(len(english_set.symmetric_difference(french_set)))
