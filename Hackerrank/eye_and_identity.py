"""
Program to print numpy array of given shape with 1s on the diagonal and 0s elsewhere
"""

import numpy as np

np.set_printoptions(legacy="1.13")

N, M = map(int, input().split())
print(np.eye(N, M, k=0))
