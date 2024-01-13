"""
Prints the reverse of the given number
"""


def reverse_integer(number: int) -> int | str:
    """
    Returns the reverse of a positive integer

    Args:
        number (int): a positive integer

    Returns:
        int | str: reverse of the number
    """
    if number > 0:
        ret = int(str(number)[::-1])
    else:
        ret = "Invalid Input"

    # Return the reversed number
    return ret


# Read a number
number = int(input())

# Call the function and display the result
print(reverse_integer(number))
