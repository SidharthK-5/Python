"""
Find the inner and outer product of two given arrays.
"""

import numpy as np

array_A = np.array(input().split(), int)
array_B = np.array(input().split(), int)

print(np.inner(array_A, array_B))
print(np.outer(array_A, array_B))
