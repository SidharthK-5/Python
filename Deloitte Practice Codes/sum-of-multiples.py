"""
Prints the sum of all the multiples of 3 or 5 within the given limit
"""

def sum_of_multiples(limit: int) -> int:
    """
    Returns the sum of all the multiples of 3 or 5 within 'limit'

    Args:
        limit (int): Number within which sum is needed

    Returns:
        int: Total sum of multiples
    """
    summed_value = 0
    for number in range(limit+1):
        if number%3 == 0 or number%5 == 0:
            summed_value += number
        
    # Return the value of sum
    return summed_value
  
# Read the value of limit
limit = int(input())
# Function call
summed_value = sum_of_multiples(limit)
# Sum of multiples of 3 and 5 within the given limit
print(summed_value)