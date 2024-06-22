"""
Find the product of multiplication of two matrices.
"""

import numpy as np

N = int(input())
matrix_A = np.array([input().split() for _ in range(N)], int)
matrix_B = np.array([input().split() for _ in range(N)], int)

print(np.dot(matrix_A, matrix_B))
