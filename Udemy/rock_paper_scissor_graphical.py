"""
Simple rock-paper-scissors game using with graphical representation.
This is a simple rock-paper-scissors game that allows the user to play against the computer.
"""

import random

# Graphical representation of the symbols
# Art taken from https://ascii.co.uk/art
rock = r"""
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
"""
paper = r"""
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_| 
"""
scissors = r"""
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
"""
list_of_symbols = [rock, paper, scissors]


print("\nWelcome to ROCK-PAPER-SCISSOR game!\n")
print("You can play against the computer.")
print("The rules are simple:")
print("Rock crushes scissors.")
print("Scissors cuts paper.")
print("Paper covers rock.")
print("You can choose between rock, paper and scissors.")
print("Type 0 for rock, 1 for paper and 2 for scissors.")
print("Type 3 to exit the game.")
print("Have fun!\n")

player_choice = int(input("Player, please enter your choice (0, 1, 2 or 3): "))
if player_choice == 3:
    print("Thanks for playing!")
    exit()
elif player_choice not in ["0", "1", "2"]:
    print("Player, you chose\n", list_of_symbols[player_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose\n", list_of_symbols[computer_choice])
    if computer_choice == player_choice:
        print("It's a tie!")
    elif (
        (computer_choice == 0 and player_choice == 2)
        or (computer_choice == 1 and player_choice == 0)
        or (computer_choice == 2 and player_choice == 1)
    ):
        print("Computer wins!")
    else:
        print("Player wins!")
print("Thanks for playing!")
