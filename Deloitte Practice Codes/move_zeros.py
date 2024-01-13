"""
Read the no. of digits and the digits of an integer from input
Move all occurences of zero to the right of the integer and print it as a list
"""


def move_zeros(digits_list: list[int]) -> list[int]:
    """
    Moves all zeros in the integer list to right

    Args:
        digits_list (list[int]): Actual input number

    Returns:
        list[int]: List in which all zeros are moved to right
    """
    count = 0
    while 0 in digits_list:
        digits_list.remove(0)
        count += 1
    digits_list.extend([0] * count)
    return digits_list


# Read the variable from STDIN
a = int(input())
digits_list = []
for i in range(a):
    digits_list.append(int(input()))

digits_list = move_zeros(digits_list)

# Output the variable to STDOUT
print(digits_list)
