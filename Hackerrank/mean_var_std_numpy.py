"""
Print the mean, var, and std of the given array along the given axes.
"""

import numpy as np


N, M = map(int, input().split())
array = np.array([input().split() for _ in range(N)], int)

print(np.mean(array, axis=1))
print(np.var(array, axis=0))
print(round(np.std(array), 11))
