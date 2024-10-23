"""
Program to perform binary search on a sorted list
"""

def binary_search(array, search_key):
    """
    Perform a binary search on a sorted array to find the index of a given search key.
    Args:
        array (list): The list of elements to search through. The list does not need to be sorted beforehand.
        search_key (Any): The element to search for in the array.
    Returns:
        int: The index of the search_key in the array if found, otherwise -1.
    """
    array = sorted(array)
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == search_key:
            return mid
        elif array[mid] < search_key:
            start = mid + 1
        else:
            end = mid - 1

    return -1


if __name__ == "__main__":
    array = list(map(int, input("Enter the list of numbers: ").split()))
    target = int(input("Enter the number to search: "))
    index = binary_search(array, target)
    if index != -1:
        print(f"{target} found at index: {index}")
    else:
        print(f"{target} not found")