"""
Program to demonstrate the use of try-except block in Python
"""

N = int(input())
test_cases = [input().split() for _ in range(N)]
for test_case in range(N):
    try:
        print(int(test_cases[test_case][0]) // int(test_cases[test_case][1]))
    except ZeroDivisionError as error:
        print("Error Code:", error)
    except ValueError as error:
        print("Error Code:", error)
