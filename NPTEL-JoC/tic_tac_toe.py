import numpy

game_board = numpy.array([['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']])

player_one_symbol = 'X'
player_two_symbol = 'O'

def check_rows(symbol):
    for row in range(3):
        count = 0
        for col in range(3):
            if game_board[row][col] == symbol:
                count += 1
        if count == 3:
            return True
    return False


def check_cols(symbol):
    for col in range(3):
        count = 0
        for row in range(3):
            if game_board[row][col] == symbol:
                count += 1
        if count == 3:
            return True
    return False


def check_diagonals(symbol):
    if game_board[0][2] == game_board[1][1] and game_board[1][1] == game_board[2][0] and game_board[1][1] == symbol:
        return True
    elif game_board[0][0] == game_board[1][1] and game_board[1][1] == game_board[2][2] and game_board[1][1] == symbol:
        return True
    return False


def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)


def place_symbol(symbol):
    print(numpy.matrix(game_board))

    while True:
        row = int(input("Enter row: 1, 2 or 3: "))
        col = int(input("Enter column: 1, 2 or 3: "))
        if row>0 and row<4 and col>0 and col<4 and game_board[row-1][col-1] == '_':
            break
        else:
            print("Invalid input. Please enter correct input again")

    game_board[row-1][col-1] = symbol


def play():
    for turn in range(9):
        if turn%2 == 0:
            print("\nX's turn")
            place_symbol(player_one_symbol)
            if won(player_one_symbol):
                print("\n'X' WON...")
                break
        else:
            print("\nO's turn")
            place_symbol(player_two_symbol)
            if won(player_two_symbol):
                print("\n'O' WON...")
                break
    
    if not(won(player_one_symbol)) and not(won(player_two_symbol)):
        print("\nMATCH DRAW...")

if __name__ == "__main__":
    play()