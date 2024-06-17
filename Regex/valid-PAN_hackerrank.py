"""
Program to find valid PAN number from a given no. of inputs
"""


import re

N = int(input())
test_cases = []
pattern = r"[A-Z]{5}\d{4}[A-Z]"

# Accepting test cases
for _ in range(N):
    test_cases.append(input())

# Checking for valid PAN number
for case in test_cases:
    if re.match(pattern, case):
        print("YES")
    else:
        print("NO")
