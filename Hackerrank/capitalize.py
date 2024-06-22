"""
Program to capitalize the first letter of each word in a string
"""


def solve(string: str) -> str:
    """
    Capitalize the first letter of each word in a string

    Args:
        string (str): Input string to be capitalized

    Returns:
        str: Capitalized string
    """
    return " ".join([word.capitalize() for word in string.split(" ")])


if __name__ == "__main__":
    string = input()
    print(solve(string))
