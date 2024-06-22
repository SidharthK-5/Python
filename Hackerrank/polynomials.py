"""
Find the value of polynomial at a given point.
"""

import numpy as np

coefficients = list(map(float, input().split()))
value_point = float(input())

print(np.polyval(coefficients, value_point))
