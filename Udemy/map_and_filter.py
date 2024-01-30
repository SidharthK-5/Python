"""
map() and filter() in Python
"""


def sqaured(number: float) -> float:
    """
    Find the square of a number

    Args:
        number (float): number whose sqaure is to be found

    Returns:
        float: sqaure of input
    """
    return number**2


def add_numbers(number_1: float, number_2: float) -> float:
    """
    Find sum of two numbers

    Args:
        number_1 (float): Number 1
        number_2 (float): Number 2

    Returns:
        float: Sum of number 1 and number 2
    """
    return number_1 + number_2


def multiple_of_20(number: int) -> bool:
    """
    Checks if the number is multiple of 20 or not

    Args:
        number (int): Number to check

    Returns:
        bool: True or False if the number is a multiple or not respectively
    """
    if number % 20 == 0:
        return True
    else:
        return False


"""
map() function
It takes two arguments: a function and an iterable
map() will apply the function to each element in the iterable and return the result
"""

sample_list = [10, 20, 30, 40, 50]
print(f"{sample_list=}")

sample_list_sqaured = list(map(sqaured, sample_list))
print(f"\n{sample_list_sqaured=}")

summed_list = list(map(add_numbers, sample_list, sample_list_sqaured))
print(f"\nList of sum of elements from above two lists: {summed_list}")

"""
filter() function
It takes two arguments: a function and an iterable
filter() will return a result with the iterable elements that satisfy the function
"""

multiples_of_twenty = list(filter(multiple_of_20, sample_list))
print(f"\nMultiples of 20 from sample_list: {multiples_of_twenty}")
