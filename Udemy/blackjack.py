import random

from art import logo


def deal_card():
    available_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(available_cards)
    return card


def calculate_score(cards: list):
    if sum(cards) == 21 and len(cards) == 2:
        # This represents Blackjack
        return 0

    if 11 in cards and sum(cards) > 21:
        # Use value of Ace as 1 instead of 11
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_blackjack():
    user_score = -1
    computer_score = -1
    is_game_over = False
    user_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]

    print(logo)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"\tComputer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            player_choice = input("Type 'y' to hit (another card), or 'n' to pass: ")
            if player_choice == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True  # Since user does not want to continue

    while computer_score != 0 and computer_score < 17:
        # If computer score is below 17, it has to keep on selecting cards till it crossed 17
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 3)
    play_blackjack()
