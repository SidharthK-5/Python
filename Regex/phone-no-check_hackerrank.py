"""
Question:
Given some numbers. Find if they are valid phone numbers or not
Criteria:
1. Total no. of digits = 10
2. Should start with either 7, 8 or 9
"""

import re

valid_phone = "^[7-9][0-9]{9}$"
N = int(input())
test_cases = []
for test_case in range(N):
    row = input()
    test_cases.append(row)

for test_case in test_cases:
    if re.match(valid_phone, test_case):
        print("YES")
    else:
        print("NO")
