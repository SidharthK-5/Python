"""
Program to check if the given string has Alphanumeric, Alphabets, Digits, Lowercase letters and Uppercase letters
"""

import re

if __name__ == "__main__":
    string = input()

    print(bool(re.search("\w", string)))  # Check for alnum
    print(bool(re.search("[a-zA-Z]", string)))  # Check for alphabets
    print(bool(re.search("\d", string)))  # Check for digits
    print(bool(re.search("[a-z]", string)))  # Check for lowercase letters
    print(bool(re.search("[A-Z]", string)))  # Check for uppercase letters
