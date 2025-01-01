"""
Python implementation of the bubble sort algorithm.
"""


def bubble_sort(array):
    """
    Sorts an array of numbers using the bubble sort algorithm.

    Args:
        array (list): A list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.

    The function works by repeatedly stepping through the list, comparing adjacent
    elements and swapping them if they are in the wrong order. This process is repeated
    until the list is sorted. If no swaps are made during a pass, the list is considered
    sorted and the function terminates early.
    """
    array_length = len(array)
    for i in range(array_length):
        # Track if any swap happens
        swapped = False
        for j in range(0, array_length - i - 1):
            if array[j] > array[j + 1]:
                # Swap the elements
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        # If no swap happened, the array is already sorted
        if not swapped:
            break
    return array


# Example usage
if __name__ == "__main__":
    array = list(
        map(int, input("Enter the array elements separated by space: ").split())
    )
    print(f"Sorted array: {bubble_sort(array)}")
