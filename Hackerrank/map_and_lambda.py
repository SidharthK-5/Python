"""
Given a number n. Create a Fibonacci sequence of n terms
Use map and lambda functions to print a list of cubes of the fibonacci terms
"""

cube = lambda x: x**3  # noqa: E731


def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        fibonacci_sequence = [0, 1]
        for i in range(2, n):
            fibonacci_sequence.append(
                fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
            )
        return fibonacci_sequence


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
