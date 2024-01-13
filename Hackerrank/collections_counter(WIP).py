"""
Raghu is a shoe shop owner. His shop has 'num_of_shoes' number of shoes.
He has a list 'available_shoes' containing the size of each shoe he has in his shop.
There are number of customers who are willing to pay some
amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
"""

num_of_shoes = int(input())  # No of shoes
available_shoes = input().split()  # diff sizes of shoes available
num_of_customers = int(input())  # No of customers waiting
need_list = []  # list to store user needs
total_cost = 0
for customer_need in range(num_of_customers):
    # Loop taking user inputs line by line
    # user will input the size they need and the amount they are willing to pay [size, price]
    row = input().split()
    need_list.append(row)

for customer in range(num_of_customers):
    shoe = need_list[customer][0]  # the shoe size the current customer needs
    if shoe in available_shoes:
        # if required shoe size is present, add price
        total_cost += int(
            need_list[customer][1]
        )  # Add the price promised by the customer
        available_shoes.remove(shoe)  # Remove the shoe from the list since it's taken

print(total_cost)
