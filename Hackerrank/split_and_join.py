"""
Program to split a sentence at white space and join them with '-'
"""


def split_and_join(line: str) -> str:
    """
    Splits the sentence at white space and join them with '-'

    Args:
        line (str): String to be modified

    Returns:
        str: String joined with '-'
    """
    l = line.split(" ")
    l = "-".join(l)
    return l


if __name__ == "__main__":
    line = input()
    print(split_and_join(line=line))
