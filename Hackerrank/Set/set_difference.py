"""
Example of set difference operation
"""

# Read two sets from input
n = int(input())
english_set = set(map(int, input().split()))
b = int(input())
french_set = set(map(int, input().split()))

# Length of english set after difference
print(len(english_set.difference(french_set)))
