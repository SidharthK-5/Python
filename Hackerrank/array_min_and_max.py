"""
Given a 2-D array with dimensions N x M
Task is to find the min along axis 1 and then find the max of that.
"""

import numpy as np


def min_and_max(array: np.array) -> int:
    return np.max(np.min(array, axis=1))

if __name__ == '__main__':
    N, M = map(int, input().split())
    array = np.array([input().split() for _ in range(N)], int)
    print(min_and_max(array))