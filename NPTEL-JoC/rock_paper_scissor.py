"""
Program to play Rock-Paper-Scissor game
"""

import getpass


GAME_KEYS = {1: "rock", 2: "paper", 3: "scissors"}


def compare_user_inputs(player_one_choice, player_two_choice):
    """
    Compares the choices of two players in a game of Rock, Paper, Scissors and determines the winner.

    Parameters:
    player_one_choice (str): The choice of the first player. Should be one of 'rock', 'paper', or 'scissors'.
    player_two_choice (str): The choice of the second player. Should be one of 'rock', 'paper', or 'scissors'.

    Returns:
    str: A message indicating the result of the game:
         - "It's a tie!" if both players chose the same option.
         - "Player one wins!" if the first player's choice beats the second player's choice.
         - "Player two wins!" if the second player's choice beats the first player's choice.
         - "Invalid input!" if either player's choice is not one of 'rock', 'paper', or 'scissors'.
    """
    print(
        f"Player 1 chose {player_one_choice.upper()} and Player 2 chose {player_two_choice.upper()}"
    )
    if player_one_choice == player_two_choice:
        return "It's a tie!"
    elif player_one_choice == "rock":
        if player_two_choice == "scissors":
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif player_one_choice == "paper":
        if player_two_choice == "rock":
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif player_one_choice == "scissors":
        if player_two_choice == "paper":
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    else:
        return "Invalid input!"


print("\nWelcome to Rock-Paper-Scissors game!\n")
print("Enter your choice as 1 (rock), 2 (paper), or 3 (scissors).\n")
while True:
    player_one_choice = GAME_KEYS.get(
        int(getpass.getpass("Player 1, enter your choice: ")), "Invalid input!"
    )
    player_two_choice = GAME_KEYS.get(
        int(getpass.getpass("Player 2, enter your choice: ")), "Invalid input!"
    )
    print(compare_user_inputs(player_one_choice, player_two_choice))
    play_again = input("\nDo you want to play again? ([y]/n): \n")
    if play_again.lower() == "n":
        break
