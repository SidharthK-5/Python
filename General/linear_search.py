"""
Program to search for a number in a list using linear search
"""


def linear_search(array, target):
    """
    Perform a linear search on the given array to find the target value.

    Args:
        array (list): The list of elements to search through.
        target: The value to search for in the array.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


if __name__ == "__main__":
    array = list(map(int, input("Enter the list of numbers: ").split()))
    target = int(input("Enter the number to search: "))
    index = linear_search(array, target)
    if index != -1:
        print(f"{target} found at index {index}")
    else:
        print(f"{target} not found")
