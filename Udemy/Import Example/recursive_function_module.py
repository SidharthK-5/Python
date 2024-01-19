"""
This module contains binary search implementation using recursion
"""


def binary_search(input_list: list[int], search_value: int) -> bool:
    """
    Search for a particular value in the given list

    Args:
        input_list (list[int]): List in which search is to be done
        search_value (int): Value to search

    Returns:
        bool: True if the search value is present in the list and False otherwise
    """
    if len(input_list) == 0:
        return False
    else:
        mid = len(input_list) // 2
        if input_list[mid] == search_value:
            return True
        elif search_value < input_list[mid]:
            return binary_search(input_list[:mid], search_value)
        else:
            return binary_search(input_list[mid + 1 :], search_value)


if __name__ == "__main__":
    int_list = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    search_value = 700
    result = binary_search(input_list=int_list, search_value=search_value)
    print(result)
