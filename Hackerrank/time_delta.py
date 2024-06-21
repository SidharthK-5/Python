"""
Program to find the difference between two timestamps in seconds of given test cases.
"""

from datetime import datetime

date_format = "%a %d %b %Y %H:%M:%S %z"

N = int(input())
test_cases = []
for _ in range(N):
    test_cases.append((input(), input()))  # Takes in two lines of input

for test_case in test_cases:
    t1 = datetime.strptime(test_case[0], date_format)
    t2 = datetime.strptime(test_case[1], date_format)
    print(int(abs((t1 - t2).total_seconds())))
