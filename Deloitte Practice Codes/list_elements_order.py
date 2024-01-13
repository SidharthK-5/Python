"""
Program to check if the elements in the given input list are in ascending order or not
"""


def ascending(input_list: list[int]) -> bool:
    """
    Checks if the given list elements are in ascending order or not

    Args:
        input_list (list[int]): The input list whose order is to be checked

    Returns:
        bool: Order status of the list
    """

    if input_list == sorted(input_list):
        ret = True
    else:
        ret = False
    return ret


input_values = list(
    map(int, input().split(","))
)  # Read the input as a list of integers

result = ascending(input_values)
print(result)
