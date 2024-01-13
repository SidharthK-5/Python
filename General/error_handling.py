"""
Error handling example with try...except
"""


def get_list_item(input_list: list[int], index: int) -> int | None:
    """
    Finds if the given index is present in the list or not

    Args:
        input_list (list[int]): List in which index is checked
        index (int): The index to be found

    Returns:
        int | None: Value at index or None if index is not present
    """
    try:
        return input_list[index]
    except IndexError:
        return None


def multiply_strings(string: str, multiplier: int = 3) -> str:
    """
    Multiply a string give nnumbre of times

    Args:
        string (str): The string to be multiplied
        multiplier (int, optional): How many times the string is to be multiplied. Defaults to 3.

    Raises:
        ValueError: If multiplier is less than 0

    Returns:
        str: Multiplied string
    """
    if multiplier < 0:
        raise ValueError("y must be greater than 0")

    multiplied_string = string * multiplier
    output = multiplied_string + "!!"
    return output


my_list = [1, 2, 3, 4, 5, 6, 7]
print(get_list_item(input_list=my_list, index=8))

print(multiply_strings(string="Yay", multiplier=5))
