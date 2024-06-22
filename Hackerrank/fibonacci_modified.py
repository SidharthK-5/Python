"""
Fibonacci Modified Series: T(i+2) = T(i)) + T(i+1)^2

Given T(1), T(2), N, find T(N)
"""

import sys

sys.set_int_max_str_digits(1000000)


def fibonacci_modified(first_term: int, second_term: int, n: int) -> int:
    """
    Returns the Nth term of the Fibonacci Modified Series

    Args:
        first_term (int): First term of the modified Fibonacci series
        second_term (int): Second term of the modified Fibonacci series
        n (int): The term to be found

    Returns:
        int: The Nth term of the modified Fibonacci series
    """
    if n == 1:
        return first_term
    elif n == 2:
        return second_term
    for _ in range(3, n + 1):
        third_term = first_term + second_term**2
        first_term = second_term
        second_term = third_term
    return third_term


first_term, second_term, n = map(int, input().split())
print(fibonacci_modified(first_term, second_term, n))
