"""
Variable Type and ID in Python
"""

# Variable type and id
first = 5
second = 50
print(f"Variable values are: {first=} & {second=}")
print(f"Type of first: {type(first)} & Type of second: {type(second)}")
print(f"ID of first: {id(first)} & ID of second: {id(second)}")

"""
Object intering
Means if two variables are having same value, both of their id's will be same
"""

a = 10
b = 10

print(f"New variable values are: {a=} & {b=}")
print(f"ID of first: {id(a)} & ID of second: {id(b)}")
