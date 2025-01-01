from PIL import Image
from random import randint

GAME_DATA = {
    9: 27,
    16: 7,
    18: 37,
    25: 54,
    28: 51,
    56: 64,
    59: 17,
    63: 19,
    67: 30,
    68: 88,
    76: 97,
    79: 100,
    87: 24,
    93: 69,
    95: 75,
    99: 77,
}


def show_board():
    image = Image.open("data/snake_and_ladder.png")
    image.show()
    image.close()


def check_snake_or_ladder(position: int) -> int:
    if position in GAME_DATA:
        new_position = GAME_DATA[position]
        if new_position > position:
            print("Congrats! You got a ladder!")
        else:
            print("Oops! You got a snake!")
        return new_position
    return position


def handle_turn(player_name: str, player_position: int) -> tuple[int, int]:
    dice_value = randint(1, 6)
    print(f"{player_name} rolled a {dice_value}")
    player_position += dice_value
    player_position = check_snake_or_ladder(player_position)
    if player_position > 100:
        print("Current position is greater than 100. Try again!")
        player_position -= dice_value
    return player_position, dice_value


def play():
    # Get player names
    player_one = input("Enter player 1 name: ")
    player_two = input("Enter player 2 name: ")
    player_one_position = 0
    player_two_position = 0

    # Game loop
    turn = 0
    while True:
        if turn % 2 == 0:
            # Player 1's turn
            print(f"\n{player_one}'s turn")
            player_one_position, dice_value = handle_turn(
                player_one, player_one_position
            )
            if player_one_position == 100:
                print(f"{player_one} wins!")
                break
            if dice_value != 6:
                turn += 1
        else:
            # Player 2's turn
            print(f"\n{player_two}'s turn")
            player_two_position, dice_value = handle_turn(
                player_two, player_two_position
            )
            if player_two_position == 100:
                print(f"{player_two} wins!")
                break
            if dice_value != 6:
                turn += 1
        print(f"{player_one} is at {player_one_position}")
        print(f"{player_two} is at {player_two_position}")

        # Ask players if they want to continue
        if input("\nDo you want to continue playing? (y/n): ").lower() == "n":
            break


if __name__ == "__main__":
    show_board()
    play()
