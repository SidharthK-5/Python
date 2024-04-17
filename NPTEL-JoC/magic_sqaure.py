"""
Program to create a magic square of size 3
Sample 3x3 magic sqaure
    2 7 6
    9 5 1
    4 3 8
"""


def print_magic_square(magic_sqaure: list):
    for row in magic_sqaure:
        for item in row:
            print(item, end=" ")
        print()


def magic_square(size: int = 3) -> list[int]:
    """
    Generates a sqaure of 0's with size of 'size'. Defaulted to 3.

    Args:
        size (int): Size of the square to be made.

    Returns:
        list[int]: Sqaure of given size.
    """
    magic_square = [[0 for i in range(size)] for j in range(size)]

    # Starting row index should be size//3 and column index should be size-1
    row_idx = size // 2
    col_idx = size - 1
    count = 1
    numbers = size**2  # Count of nos to be filled = square of size

    while count <= numbers:
        if row_idx == -1 and col_idx == size:
            # When both row_idx and col_idx goes out of index together
            col_idx = size - 2
            row_idx = 0
        else:
            if col_idx == size:  # column value is exceeding
                col_idx = 0
            if row_idx < 0:  # row = - 1
                row_idx = size - 1

        if magic_square[row_idx][col_idx] != 0:
            # If the current location is already occupied
            col_idx = col_idx - 2
            row_idx = row_idx + 1
            continue
        else:
            # Placing current number in an empty location
            magic_square[row_idx][col_idx] = count
            count += 1

        # Update row and col after each iteration
        row_idx -= 1
        col_idx += 1

    print("Magic square of size 3x3:")
    for i in range(size):
        for j in range(size):
            print(magic_square[i][j], end=" ")
        print()

    print(f"Sum of each row/column/diagonal = {size*(size**2 + 1)//2}")


magic_square(3)
