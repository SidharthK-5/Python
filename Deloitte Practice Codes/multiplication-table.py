"""
Enter the number of tables needed.
In the subsequesnt lines, enter the numbers who's multiplication table is needed.
Final output is the multiplication table of all these numbers upto 10
"""

no_of_tables = int(input())
numbers = []
for number in range(no_of_tables):
    numbers.append(int(input()))

for number in numbers:
    for i in range(1,11):
        print("{} x {} = {}".format(number, i, number*i))
    print("===============")
