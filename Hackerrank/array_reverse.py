"""
Given a space separated list of numbers
Reverse the list of numbers by converting them into a numpy array.
"""

import numpy

def arrays(arr):
    arr = numpy.array(arr, float)
    return arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)