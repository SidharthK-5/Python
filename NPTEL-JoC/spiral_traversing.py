def spiral(total_rows, total_cols, array):
    row_iter = 0
    col_iter = 0

    # row_iter - starting row index, col_iter - starting column index
    while row_iter < total_rows and col_iter < total_cols:
        # Print first row from the remaining rows
        for i in range(col_iter, total_cols):
            print(array[row_iter][i], end=" ")
        row_iter += 1

        # Print the last column from the remaining columns
        for i in range(row_iter, total_rows):
            print(array[i][total_cols - 1], end=" ")
        total_cols -= 1

        if row_iter < total_rows:
            # Print the last row from the remaining rows
            for i in range(total_cols - 1, col_iter - 1, -1):
                print(array[total_rows - 1][i], end=" ")
            total_rows -= 1

        if col_iter < total_cols:
            # Print the first column from the remaining columns
            for i in range(total_rows - 1, row_iter - 1, -1):
                print(array[i][col_iter], end=" ")
            col_iter += 1


if __name__ == "__main__":
    array = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
    rows = 3
    cols = 6

    for i in range(rows):
        for j in range(cols):
            print(array[i][j], end="\t")
        print()

    print("\nSpiral Traversing of the given matrix is:")
    spiral(rows, cols, array)
