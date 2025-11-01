"""
Demonstration of NumPy arrays and their operations.
"""

import numpy as np

# Array of zeros
zeros_array = np.zeros((3, 4))
print("Array of zeros:\n", zeros_array)
print("Shape of zeros array:", zeros_array.shape)

# Array of ones
ones_array = np.ones((2, 5))
print("\nArray of ones:\n", ones_array)
print("Shape of ones array:", ones_array.shape)

# Array with a specific value
fives_array = np.full((4, 3), 5)
print("\nArray filled with fives:\n", fives_array)
print("Shape of fives array:", fives_array.shape)

# Create a 2x2 array with random values
random_array = np.random.random((2, 2))
print("\nArray with random values:\n", random_array)
print("Shape of random array:", random_array.shape)

# Array with specified dtype
dtyped_array = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64)
print("\nArray with specified dtype (int64):\n", dtyped_array)
print("Dtype of the array:", dtyped_array.dtype)
