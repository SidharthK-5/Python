"""
Jumble words game for two players
"""

import random


words = [
    'rainbow', 'computer', 'programming', 'mathematics','player', 'condition', 'reverse', 'water', 'board'
]

def choose() -> str:
    """
    Chooses a word from the given list of strings

    Returns:
        str: a randomly picked word
    """
    pick = random.choice(words)
    return pick


def jumble(word: str) -> str:
    """
    Generates a jumbled of the given word

    Args:
        word (str): the word to be jumbled

    Returns:
        str: the jumbled word
    """
    word_length = len(word)
    jumbled = ''.join(random.sample(word, word_length))
    return jumbled


def thank(player_one_name: str, player_two_name: str, player_one_score: int, player_two_score: int) -> str:
    """
    Creates a thanks message after game completion

    Args:
        player_one_name (str): Name of player 1
        player_two_name (str): Name of player 2
        player_one_score (int): Score of player 1
        player_two_score (int): Score of player 2

    Returns:
        str: Final thanks message with player scores
    """
    player_one_msg = f"{player_one_name}, your score is: {player_one_score}"
    player_two_msg = f"{player_two_name}, your score is: {player_two_score}"
    greeting_msg = "Thanks for playing \nHave a nice day!!"
    final_msg = player_one_msg + '\n' + player_two_msg + '\n' + greeting_msg
    return final_msg


def one_turn(player_name: str, player_score: int, answer: str) -> int:
    """
    Lets the player to guess the answer and updates the score accordingly

    Args:
        player_name (str): Player name in the current turn
        player_score (int): Player score in the current turn
        answer (str): Actual answer in the round

    Returns:
        int: Updated player score from the current round
    """
    print(f"{player_name}, your turn")
    guessed_word = input("Enter your guess: ")
    if guessed_word.lower() == answer:
        player_score += 1
        print(f"You guessed it right!! Your score: {player_score}")
    else:
        print(f"Wrong guess :(. Actual answer is: {answer}")
        
    return player_score
    

def play():
    # Receive player names from input
    player_one_name = input("Player 1, please enter your name: ")
    player_two_name = input("Player 2, please enter your name: ")
    # Initializing players' scores to zero
    player_one_score = 0
    player_two_score = 0
    
    turn = 0 # keeps track of which player is having the current turn
    while True:
        # Logic to generate jumbled word for the player
        picked_word = choose()
        question = jumble(word=picked_word)
        print(f"\nJumbled question word: {question}")
        
        # If turn is even, player 1 plays, else player 2
        if turn % 2 == 0:
            player_one_score = one_turn(player_name=player_one_name, player_score=player_one_score, answer=picked_word)
            game_control = input("\nDo you want to continue ([y]/n): ")
            
            # Stop the game as per current player's choice
            if game_control.lower() == 'n':
                print(thank(player_one_name, player_two_name, player_one_score, player_two_score))
                break
            
        else:
            player_two_score = one_turn(player_name=player_two_name, player_score=player_two_score, answer=picked_word)
            game_control = input("\nDo you want to continue ([y]/n): ")
            
            # Stop the game as per current player's choice
            if game_control.lower() == 'n':
                print(thank(player_one_name, player_two_name, player_one_score, player_two_score))
                break
        
        # update value of turn
        turn += 1


if __name__ == '__main__':
    play()