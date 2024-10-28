"""
Given two integer arrays, A and B of dimensions N x M
Perform the following operations:
    1. Sum the two arrays
    2. Subtract the two arrays
    3. Multiply the two arrays
    4. Integer division of the two arrays
    5. Modulo of the two arrays
    6. Power of the two arrays
"""

import numpy as np

N, M = map(int, input().split())
A = np.array([input().split() for _ in range(N)], int)
B = np.array([input().split() for _ in range(N)], int)

print(np.add(A, B))
print(np.subtract(A, B))
print(np.multiply(A, B))
print(np.floor_divide(A, B))
print(np.mod(A, B))
print(np.power(A, B))