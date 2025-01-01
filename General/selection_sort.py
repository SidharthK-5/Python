"""
Python program to implement selection sort
"""


def selection_sort(array):
    """
    Sorts an array using the selection sort algorithm.

    Args:
        array (list): A list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.

    The selection sort algorithm sorts an array by repeatedly finding the minimum element
    (considering ascending order) from the unsorted part and putting it at the beginning.
    The algorithm maintains two subarrays in a given array:
    1. The subarray which is already sorted.
    2. The remaining subarray which is unsorted.
    """
    array_length = len(array)
    for i in range(array_length):
        min_index = i
        for j in range(i + 1, array_length):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array


if __name__ == "__main__":
    array = list(
        map(int, input("Enter the array elements separated by space: ").split())
    )
    print(f"Sorted array: {selection_sort(array)}")
