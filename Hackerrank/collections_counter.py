"""
Raghu is a shoe shop owner. His shop has 'num_of_shoes' number of shoes.
He has a list 'available_shoes' containing the size of each shoe he has in his shop.
There are number of customers who are willing to pay some
amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
"""

from collections import Counter

num_of_shoes = int(input())  # No of shoes
available_shoes = input().split()  # diff sizes of shoes available
num_of_customers = int(input())  # No of customers waiting
total_cost = 0

available_shoes = dict(Counter(available_shoes))

for customer_need in range(num_of_customers):
    size, price = map(int, input().split())
    if available_shoes.get(str(size), 0) > 0:
        # Update the total cost and reduce the available shoes
        total_cost += price
        available_shoes[str(size)] -= 1

print(total_cost)
