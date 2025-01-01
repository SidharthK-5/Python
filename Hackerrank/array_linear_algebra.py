"""
Given an NxN matrix, A
Calculate the determinant of the A
"""

import numpy as np


N = int(input())
A = np.array([input().split() for _ in range(N)], float)
print(round(np.linalg.det(A), 2))
