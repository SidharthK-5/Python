"""
Example of set union operation
"""

# Read two sets from input
n = int(input())
english_set = set(map(int, input().split()))
b = int(input())
french_set = set(map(int, input().split()))

# Length of english set after union
print(len(english_set.union(french_set)))
