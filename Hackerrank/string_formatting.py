def print_formatted(limit_num: int) -> None:
    """
    Prints the decimal, octal hexadecimal and binary equivalents of all numbers till specified limit.
    The padding between numbers in a row is decided based on binary equivalent of limit_num

    Args:
        limit_num (int): The number within which equivalents are needed
    """
    thickness = len(bin(limit_num)) - 1
    for num in range(1, limit_num + 1):
        # Each equivalent is sliced [2:] to remove the format specifying characters from it
        print(
            str(num).rjust(thickness - 1)
            + oct(num)[2:].rjust(thickness)
            + hex(num)[2:].upper().rjust(thickness)
            + bin(num)[2:].rjust(thickness)
        )


if __name__ == "__main__":
    number = int(input())
    print_formatted(number)
