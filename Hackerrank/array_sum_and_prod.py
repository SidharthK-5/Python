"""
Given a 2-D array of dimension N x M
Find the product of the sum taken along axis 0
"""

import numpy as np


def sum_and_prod(array: np.array) -> int:
    return np.prod(np.sum(array, axis=0))


if __name__ == "__main__":
    N, M = map(int, input().split())
    array = np.array([input().split() for _ in range(N)], int)
    print(sum_and_prod(array))