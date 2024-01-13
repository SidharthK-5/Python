"""
Generating a rangoli of alphabets based on the entered size

sample input:
    3
output:
    ----c----
    --c-b-c--
    c-b-a-b-c
    --c-b-c--
    ----c----
"""


def print_rangoli(size):
    string = "abcdefghijklmnopqrstuvwxyz"
    rangoli = []
    total_rows = 2 * size - 1  # No of rows = 2*size-1
    chars_in_a_row = 4 * size - 3  # No of chara in a row = 2*(2*n-2)+1 = 4n-4+1 = 4n-3

    # Create a 2D list of only '-'
    for _ in range(total_rows):
        rangoli.append(["-"] * (chars_in_a_row))

    for row in range(size):
        string_index = size - 1
        col_start = (
            chars_in_a_row // 2 - 2 * row
        )  # In each row, the starting pos will be center - 2*row_number
        col_end = chars_in_a_row // 2 + 1  # Ending pos will be the center

        # From start to end, change the alternating character
        for col in range(col_start, col_end, 2):
            rangoli[row][col] = string[string_index]
            rangoli[row][-col - 1] = string[string_index]
            string_index -= 1
        rangoli[-row - 1] = rangoli[
            row
        ]  # Mirror the current row w.r. to the middle row

    for i in range(total_rows):
        for j in range(chars_in_a_row):
            print(rangoli[i][j], end="")
        print()


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
