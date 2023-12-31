"""
A hand cricket game between user and computer
"""

import random

num_options = [1,2,3,4,5,6]
toss_options = ['ODD', 'EVEN']
player_role = ['BAT', 'BALL']

def choice() -> int:
    """
    Lets the user choose a number between 1 and 6

    Returns:
        int: chosen number by user
    """
    while True:
        user_choice = int(input("Enter a number between 1-6: "))
        if user_choice not in num_options:
            print("Invalid Input!! \nRe-enter a number in the given range: ")
        else:
            break
    return user_choice

def toss() -> str:
    """
    Lets the user choose toss option ODD/EVEN

    Returns:
        str: chosen toss value by user
    """
    while True:
        user_toss=input("Choose \'ODD\' or \'EVEN\': ").upper()
        if user_toss not in toss_options:
            print("Invalid Input!! \nRe-enter your toss: ")
        else:
            break
    return user_toss

def role_selection(role: str) -> str:
    """
    Assigns 2nd player role based on the 1st player role

    Args:
        role (str): 1st player role

    Returns:
        str: 2nd player role
    """
    if role == 'BAT':
        return 'BALL'
    else:
        return 'BAT'

def compare_choice(toss_result: str, user_toss: str) -> list[str]:
    """
    Compare the toss results with user's choice
    and selecting role for both players

    Args:
        toss_result (str): toss result after comparing user's and computer's inputs
        user_toss (str): the toss value picked by user

    Returns:
        list[str]: user's role and computer's role
    """
    if toss_result == user_toss:
        print("\nUser won the toss\n")
        user_role = input("Choose BAT or BALL: ").upper()
        comp_role = role_selection(role=user_role)
        print(f"User chose to: {user_role} \nComputer will: {comp_role}\n")
    else:
        print("\nComputer won the toss\n")
        comp_role = random.choice(player_role)
        user_role = role_selection(role=comp_role)
        print(f"Computer chose to: {comp_role} \nUser will: {user_role}\n")

    return [user_role, comp_role]

def first_batting(player: str) -> int:
    """
    Handles the first batting logic

    Args:
        player (str): player who is batting 1st

    Returns:
        int: runs score in first batting 
    """
    runs = 0
    while True:
        comp_choice = random.choice(num_options)
        user_choice = choice()
        print(f"Computer chose: {comp_choice}")
        if comp_choice != user_choice and player == 'user':
            runs += user_choice
        elif comp_choice != user_choice and player == 'computer':
            runs += comp_choice
        else:
            print(f"\n{player.upper()} is out. Innings over!!!\n")
            break
        print(f"{player.upper()} score: {runs}")
    return runs

def second_batting(player: str, prev_score: int) -> None:
    """
    Handles the second batting logic

    Args:
        player (str): player who is batting 2nd
        prev_score (int): runs scored by 1st batted player
    """
    runs = 0
    p2_status = True # tracks the win status of 2nd batting player
    while runs <= prev_score:
        comp_choice = random.choice(num_options)
        user_choice = choice()
        print(f"Computer chose: {comp_choice}")
        if comp_choice != user_choice and player == 'user':
            runs += user_choice
        elif comp_choice != user_choice and player == 'computer':
            runs += comp_choice
        else:
            p2_status = False
            if runs == prev_score:
                print("Match draw...")
            else:
                if player == 'user':
                    print("\nComputer won the game")
                else:
                    print("\nUser won the game")
                break
        print(f"{player.upper()} score: {runs}")

    if p2_status is True:
        print(f"{player.upper()} won the game")
    
def play(user: str):
    """
    Running logic of the game

    Args:
        user (str): role assigned to the user
    """
    # Player 1 batting
    if user == 'BAT':
        user_score = first_batting(player='user')
        print("User score: ", user_score)
        print(f"Computer needs {user_score+1} runs to win\n")
        user = 'BALL'
    else:
        comp_score = first_batting(player='computer')
        print("Computer score: ", comp_score)
        print(f"User needs {comp_score+1} runs to win\n")
        user = 'BAT'

    # Player 2 batting
    if user == 'BAT':
        second_batting(player='user', prev_score=comp_score)
    else:
        second_batting(player='computer', prev_score=user_score)


if __name__ == '__main__':
    print("\nToss begins...\n")
    user_toss = toss()
    user_choice = choice()
    comp_choice = random.choice(num_options)
    print(f"Computer chose: {comp_choice}")
    toss_value = user_choice + comp_choice # tosss_value decides whether user/computer won the toss

    if toss_value % 2 == 0:
        roles = compare_choice('EVEN', user_toss)
    else:
        roles = compare_choice('ODD', user_toss)

    user_role, comp_role = roles[0], roles[1]
    play(user_role)