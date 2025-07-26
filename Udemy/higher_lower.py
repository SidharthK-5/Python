import random

from art import higher_lower_logo as logo
from art import higher_lower_vs as vs
from clear_terminal import clear_terminal
from game_data import higher_lower_data


def pretty_print_choice(choice_data: dict) -> str:
    return f"{choice_data['name']}, a {choice_data['description']}, from {choice_data['country']}"


def verify_user_selection(user_selection: dict, other_option: dict) -> bool:
    selection_follower_count = user_selection.get("follower_count")
    other_option_follower_count = other_option.get("follower_count")
    if selection_follower_count >= other_option_follower_count:
        return True
    else:
        return False


def select_second_choice(first_choice: dict):
    second_choice = first_choice
    while second_choice == first_choice:
        second_choice = random.choice(higher_lower_data)

    return second_choice


player_points = 0
choice_a = random.choice(higher_lower_data)
choice_b = select_second_choice(first_choice=choice_a)

print(logo)
while True:
    print(f"Compare A: {pretty_print_choice(choice_a)}.")
    print(vs)
    print(f"Against B: {pretty_print_choice(choice_b)}.")
    choice = input("Who has more followers? Type 'A' or 'B':  ")

    # Compare user's selection against other option
    if choice.upper() == "A":
        result = verify_user_selection(user_selection=choice_a, other_option=choice_b)
    else:
        result = verify_user_selection(user_selection=choice_b, other_option=choice_a)

    # If user's selection is correct, increase the score and continue
    if result:
        player_points += 1
        clear_terminal()
        print(logo)
        print(f"You're right! Current score: {player_points}.")
        # Update A as B, and select a new option for B
        choice_a = choice_b
        choice_b = select_second_choice(first_choice=choice_a)
    # Otherwise print the score and end the game
    else:
        clear_terminal()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {player_points}")
        break
