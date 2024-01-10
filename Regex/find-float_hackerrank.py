"""
Question: Given the number of cases:
In each case, print if the number is float or not

REGEX pattern breakdown: ^[+-]?\d*\.\d+$
1. ^ - The pattern should start with the next group/symbol
1. [+-]? - The first character can be either '+' or '-'. '?' indicates this first character is optional
2. \d* - \d denotes any decimal number. '*' indicates this decimal can have 0 or more occurences
3. . - period symbol to separate integer part and fractional part
4. \d+ - Indicates this decimal can have 1 or more occurences

"""

import re

num_cases = int(input())
for _ in range(num_cases):
    number = input()
    print(bool(re.search(pattern="^[+-]?\d*\.\d+$", string=number)))
