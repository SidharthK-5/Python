"""
Demonstration of NumPy array operations.
"""

import numpy as np

# Create two sample arrays
array_a = np.array([[1, 2, 3], [4, 5, 6]])
array_b = np.array([[7, 8, 9], [10, 11, 12]])
print("Array A:\n", array_a)
print("Array B:\n", array_b)

# Array addition
array_sum = np.add(array_a, array_b)
print("\nArray Addition (A + B):\n", array_sum)

# Array subtraction
array_diff = np.subtract(array_a, array_b)
print("\nArray Subtraction (A - B):\n", array_diff)

# Array multiplication
array_product = np.multiply(array_a, array_b)
print("\nArray Multiplication (A * B):\n", array_product)

# Array division
array_quotient = np.divide(array_a, array_b)
print("\nArray Division (A / B):\n", array_quotient)

# Square root of each elements in array A
array_sqrt = np.sqrt(array_a)
print("\nSquare Root of Array A:\n", array_sqrt)

# Transpose of array A
array_transpose = np.transpose(array_a)
print("\nTranspose of Array A:\n", array_transpose)

# Sum of elements in array A
array_sum_elements = np.sum(array_a)
print("\nSum of elements in Array A:\n", array_sum_elements)

# Row-wise sum of array A
array_row_sum = np.sum(array_a, axis=1)
print("\nRow-wise Sum of Array A:\n", array_row_sum)

# Column-wise sum of array A
array_column_sum = np.sum(array_a, axis=0)
print("\nColumn-wise Sum of Array A:\n", array_column_sum)

# Product of elements in array A
array_product_elements = np.prod(array_a)
print("\nProduct of elements in Array A:\n", array_product_elements)

# Average of elements in array A
array_average_elements = np.average(array_a)
print("\nAverage of elements in Array A:\n", array_average_elements)

# Maximum element in array B
array_max_element = np.max(array_b)
print("\nMaximum element in Array B:\n", array_max_element)

# Minimum element in array B
array_min_element = np.min(array_b)
print("\nMinimum element in Array B:\n", array_min_element)

# Mean of elements in array B
array_mean_elements = np.mean(array_b)
print("\nMean of elements in Array B:\n", array_mean_elements)

# Standard deviation of elements in array A
array_std_elements = np.std(array_a)
print("\nStandard Deviation of elements in Array A:\n", array_std_elements)

# Dot product of array A and B
array_dot_product = np.dot(array_a, array_b.T)
print("\nDot Product of Array A and B:\n", array_dot_product)
