"""
Program to create arrays of zeros and ones based on the input shape
"""

import numpy as np


shape = tuple(map(int, input().split()))

print(np.zeros(shape=shape, dtype=int))
print(np.ones(shape=shape, dtype=int))