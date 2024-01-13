"""
Error handling example with try...except
"""


def get_list_item(lis: list[int], index: int) -> int | None:
    """
    Finds if the given index is present in the list or not

    Args:
        lis (list[int]): List in which index is checked
        index (int): The index to be found

    Returns:
        int | None: Value at index or None if index is not present
    """
    try:
        return lis[index]
    except IndexError:
        return None


def w4(x, y=3):
    if y < 0:
        raise ValueError("y must be greater than 0")


    z = x * y
    w = z + "!!"
    return w


my_list = [1, 2, 3, 4, 5, 6, 7]
print(get_list_item(lis=my_list, index=8))

print(w4("Yay", 5))
