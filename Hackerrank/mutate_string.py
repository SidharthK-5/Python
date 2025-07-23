"""
Question:
Given a string, a character and index position
Place character at index position of string
"""


def mutate_string(string: str, position: int, character: str) -> str:
    """
    Replace the character at index 'position' with new character

    Args:
        string (str): The original string
        position (int): Index position to be changed
        character (str): Character to be placed in the string

    Returns:
        str: The mutated string
    """
    mutated_string = list(string)
    mutated_string[position] = character
    mutated_string = "".join(mutated_string)
    return mutated_string


if __name__ == "__main__":
    s = input()
    i, c = input().split()
    s_new = mutate_string(string=s, position=int(i), character=c)
    print(s_new)
