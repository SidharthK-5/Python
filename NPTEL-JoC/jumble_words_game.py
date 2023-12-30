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

