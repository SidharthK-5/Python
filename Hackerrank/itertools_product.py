"""
Program to find the cartesian product of two lists
"""

from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

cartesian_product = list(product(A, B))
print(*cartesian_product)
