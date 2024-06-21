"""
Program to print the transpose and flatten of a given matrix
"""

import numpy as np


N, M = map(int, input().split())
array = np.array([input().split() for _ in range(N)], int)

print(np.transpose(array))
print(array.flatten())
