"""
Guess the movie name from the given code
"""

import random

MOVIES = [
    "IRON MAN",
    "ROMANCHAM",
    "KRISHH",
    "CAPTAIN AMERICA",
    "AVENGERS ENDGAME",
    "AVATAR",
    "INTERSTELLAR",
    "INCEPTION",
    "TERMINATOR",
    "EXTRACTION",
    "MEN IN BLACK",
    "OPPENHEIMER",
    "DHOOM",
]


def create_question(movie: str) -> str:
    """
    Generated a coded string from the input movie name.

    Args:
        movie (str): Movie name to be made password like.

    Returns:
        str: Coded version of movie name.
    """
    letters = list(movie)
    coded_name = []
    for letter in letters:
        if letter == " ":
            coded_name.append(" ")
        else:
            coded_name.append("*")

    coded_question = "".join(coded_name)
    return coded_question


def is_present(letter: str, movie: str) -> bool:
    """
    Checks if the letter is present in the given movie name.
    Returns True if present, and False otherwise.

    Args:
        letter (str): Letter to be found.
        movie (str): Name of the movie.

    Returns:
        bool: Status of letter present in the movie name.
    """
    letter_count = movie.count(letter.upper())
    if letter_count == 0:
        return False
    else:
        return True


def unlock(question: str, movie: str, letter: str) -> str:
    """
    Unlocks the question word with the letter present.

    Args:
        question (str): Current coded question word.
        movie (str): Actual movie.
        letter (str): Letter in the actual movie guessed by player.

    Returns:
        str: Unlocked version of coded question with letter.
    """
    actual_movie_name = list(movie)
    question_code = list(question)

    coded_name = []
    name_length = len(movie)

    for index in range(name_length):
        if (
            actual_movie_name[index] == " "
            or actual_movie_name[index] == letter.upper()
        ):
            coded_name.append(actual_movie_name[index])
        else:
            if question_code[index] == "*":
                coded_name.append("*")
            else:
                coded_name.append(actual_movie_name[index])

    coded_question = "".join(coded_name)
    return coded_question


def execute_turn(player_name: str, player_score: int) -> int:
    """
    Execute one turn of a player.

    Args:
        player_name (str): Name of the player in the current turn
        player_score (int): Current player score

    Returns:
        int: Updated score of player.
    """
    print(f"\n{player_name}, your turn")
    picked_movie = random.choice(MOVIES)
    question = create_question(movie=picked_movie)
    print(f"Guess the movie name from this code: {question}")
    modified_question = question
    not_said = True

    while not_said:
        letter = input("Enter a guess letter: ")
        if is_present(letter=letter, movie=picked_movie):
            # Unlock the character if it is present in actual movie name
            modified_question = unlock(
                question=modified_question, movie=picked_movie, letter=letter
            )
            print(f"Updated question: {modified_question}")

            decision = input("Enter 1 to guess movie or 2 to unlock another letter: ")
            if decision == "1":
                answer = input("Enter your answer: ")
                if answer.upper() == picked_movie:
                    player_score += 1
                    print("You said it right... Yay!")
                    not_said = False
                    print(f"{player_name}, your current score: {player_score}")
                else:
                    print("Wrong answer, try again...")
        else:
            print("Letter not in movie name...")

    return player_score


def play() -> None:
    player_one_name = input("Player 1, enter your name: ")
    player_two_name = input("Player 2, enter your name: ")
    player_one_score = 0
    player_two_score = 0
    turn = 0

    willing_to_continue = True
    while willing_to_continue:
        if turn % 2 == 0:
            # Player 1
            player_one_score = execute_turn(
                player_name=player_one_name, player_score=player_one_score
            )

            stop_game = input("\nDo you want to continue [y/N]? ")
            if stop_game.lower() == "n":
                print(f"{player_one_name}, your score: {player_one_score}")
                print(f"{player_two_name}, your score: {player_two_score}")
                print("\nThanks for playing")
                willing_to_continue = False
        else:
            # Player 2
            player_two_score = execute_turn(
                player_name=player_two_name, player_score=player_two_score
            )

            stop_game = input("\nDo you want to continue [y/N]? ")
            if stop_game.lower() == "n":
                print(f"{player_one_name}, your score: {player_one_score}")
                print(f"{player_two_name}, your score: {player_two_score}")
                print("\nThanks for playing")
                willing_to_continue = False

        turn += 1


play()
