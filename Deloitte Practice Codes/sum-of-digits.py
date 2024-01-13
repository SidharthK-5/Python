"""
Prints the sum of digits of a number
"""


def sum_of_digits(number: int) -> None:
    """
    Prints the sum of digits of the given number

    Args:
        number (int): a positive integer
    """
    number = str(number)
    digits = list(map(int, number))
    print(sum(digits))


# Function call
number = int(input())
sum_of_digits(number)
