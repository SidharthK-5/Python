"""
Example of set intersection operation
"""

# Read two sets from input
n = int(input())
eng_list = set(map(int, input().split()))
b = int(input())
french_list = set(map(int, input().split()))

# Length of english set after intersection
print(len(eng_list.intersection(french_list)))
