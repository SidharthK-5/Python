"""
Given a numpy array, A
Print the floor, ceil and rint of the array.
"""

import numpy as np

np.set_printoptions(legacy="1.13")  # O/p format as specified in the task

A = np.array(input().split(), float)

print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))
