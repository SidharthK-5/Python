"""
Program to convert the given list into a 3x3 matrix
"""

import numpy as np

array = np.array(list(map(int, input().split())))
print(array.reshape(3, 3))
