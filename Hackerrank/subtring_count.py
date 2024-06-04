"""
Count the no. of substrings in a given string
"""


def count_substring(string: str, sub_string: str) -> int:
    """
    Counts the no. of occurences of substring in the given string.

    Args:
        string (str): The main string.
        sub_string (str): The strings to be counted in the main one.

    Returns:
        int: No. of occurences of substring.
    """
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if sub_string == string[i : i + len(sub_string)]:
            count += 1

    return count


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string=string, sub_string=sub_string)
    print(count)
