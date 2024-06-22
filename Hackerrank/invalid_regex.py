"""
Program to find out if a given regex is valid or not
"""

# This code works only in Pypy 3
import re


N = int(input())
test_cases = [input() for _ in range(N)]
for test_case in test_cases:
    try:
        re.compile(test_case)
        print("True")
    except re.error:
        print("False")
