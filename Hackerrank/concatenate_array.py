"""
Program to concatenate two numpy arrays along axis 0
"""

import numpy as np

N, M, P = map(int, input().split())
array_1 = np.array([input().split() for _ in range(N)], int)
array_2 = np.array([input().split() for _ in range(M)], int)

print(np.concatenate((array_1, array_2), axis=0))
