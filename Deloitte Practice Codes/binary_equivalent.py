"""
Find the binary equivalent of an integer (0 < number < 1000) using while loop
"""

def decimal_to_binary(number: int) -> None:
    """
    This function converts decimal number to binary and prints it

    Args:
        number (int): The number whose binary equivalent is to be found
    """
    if number>0 and number<1000:
        binary_equivalent = []
        while number>0:
            binary_equivalent.append(str(number%2))
            number = number // 2
        print(''.join(binary_equivalent)[::-1])
    else:
        print('INVALID_INPUT')

n = int(input())        
decimal_to_binary(n)