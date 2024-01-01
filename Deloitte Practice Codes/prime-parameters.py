"""
Enter a limit number. Enter those many numbers in subsequent lines
The result will be PRIME or COMPOSITE in the order of numbers input
"""

def is_prime(number: int) -> str:
    """
    Checks if the given number is prime or composite
    if the number is in the range [2,1000]

    Args:
        number (int): The number which is to be checked

    Returns:
        str: Whether the number is prime or composite
    """
    if number<2 or number>1000:
        return "Out of Range"
    else:
        flag = 0 # Says if the variable is PRIME or COMPOSITE (0 => PRIME, 1 => COMPOSITE)
        for divisor in range(2, number//2 + 1):
            if number % divisor == 0:
                flag = 1
                break
        if flag == 1:
            return "COMPOSITE"
        else:
            return "PRIME"

total_numbers = int(input())
number_list = []
for i in range(total_numbers):
    number_list.append(int(input()))

for number in number_list:
    result = is_prime(number)
    print(result)
