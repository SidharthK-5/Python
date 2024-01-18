"""
Print the sum of all natural numbers till 'limit' and it's average
"""

limit = int(input())
numbers_list = list(range(1, limit + 1))
sum_to_limit = sum(numbers_list)
average = sum_to_limit / limit
print(f"sum={sum_to_limit}, average={average}")
