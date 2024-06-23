"""
Given a list of N items and their prices
Print the items and their prices in the order of their first occurrence
"""

from collections import OrderedDict

N = int(input())
items = OrderedDict()
for _ in range(N):
    item, price = input().rsplit(maxsplit=1)
    items[item] = items.get(item, 0) + int(price)

print("\n".join([f"{item} {price}" for item, price in items.items()]))
