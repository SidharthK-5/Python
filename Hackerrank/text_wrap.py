"""
Question: Given a string and an integer 'max_width'
            Wrap the the string by keeping only 'max_width' no. of characters in each line
"""

import textwrap


def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
