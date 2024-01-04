"""
Find the factorial of a given number
"""

n = int(input())
factorial = 1
while n > 0:
    factorial *= n
    n -= 1

print(f"{factorial=}")
