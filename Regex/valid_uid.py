"""
Find valid UID from a given samples
Valid UID:
- At least 2 uppercase English alphabet characters.
- At least 3 digits (0-9).
- Only alphanumeric characters.
- No repeating characters.
- Exactly 10 characters long.
"""

import re


uid_pattern = r"^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?=(?:[a-zA-Z0-9]){10,})(?!.*(.).*\1).{10}$"  # noqa: E501

T = int(input())
test_cases = [input() for _ in range(T)]

for test_case in test_cases:
    if re.match(uid_pattern, test_case):
        print("Valid")
    else:
        print("Invalid")
