"""
Prints the sum of all prime numbers from the given numbers
"""


def sum_primes(number_list: list[int]) -> int:
    """
    Retuns the sum of all prime numbers in number_list

    Args:
        number_list (list[int]): list of numbers

    Returns:
        int: sum of prime numbers in the number_list
    """
    sum_of_primes = 0
    for number in number_list:
        if number > 1:
            flag = 1  # Tells if number is prime/composite. 1 => Prime, 0 => Composite
            for divisor in range(2, (number // 2) + 1):
                if number % divisor == 0:
                    flag = 0
                    break
            if flag:
                sum_of_primes += number

    return sum_of_primes


# Read the list of numbers
number_list = list(map(int, input().split()))

sum_of_primes = sum_primes(number_list)
print(sum_of_primes)
