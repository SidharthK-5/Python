"""
Docstring: This module contains binary search implementation using recursion
"""


def binary_search(l, key):
    """
    Binary search : Input a list and a key
    Return will be true if key is found in the list. Else, False
    """
    if len(l) == 0:
        return False
    else:
        mid = len(l) // 2
        if l[mid] == key:
            return True
        elif key < l[mid]:
            return binary_search(l[:mid], key)
        else:
            return binary_search(l[mid + 1 :], key)


if __name__ == "__main__":
    l = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    key = 700
    result = binary_search(l, key)
    print(result)
