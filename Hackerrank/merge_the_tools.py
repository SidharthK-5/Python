"""
Given a string of length n and an integer k, split the string into n/k substrings.
Each substring contains k characters.
The characters in a substring must be distinct. Print each substring on a new line.
"""


def merge_the_tools(string, k):
    n = len(string)
    for idx in range(0, n, k):
        sub_string = string[idx : idx + k]
        characters_seen = set()
        for character in sub_string:
            if character not in characters_seen:
                print(character, end="")
                characters_seen.add(character)
        print()


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
