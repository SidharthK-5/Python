"""
Variable length argument functions using args and kwargs
"""


def add_value(*args):
    list_of_args = []
    for item in args:
        list_of_args.append(item)
    return list_of_args


# Variable length keyword argument function
def get_details(**kwargs):
    print(kwargs)


print("args: Arguments as tuples")
# Passing 5 arguments
result = add_value(100, 200, 300, 400, 500)
print(f"Arguments: {100, 200, 300, 400, 500}   {result=}")

# Passing 2 arguments
result = add_value(100, 200)
print(f"Arguments: {100, 200}   {result=}")

# Passing 8 values
result = add_value(100, 200, 300, 400, 500, 600, 700, 800)
print(f"Arguments: {100, 200, 300, 400, 500, 600, 700, 800}   {result=}")

print("\nkwargs: Arguments as dictionaries")
get_details(name="ABC", email="abc@gmail.com", contact=7123456789, dob="12/5/1870")
get_details(name="ABC", email="abc@gmail.com", dob="12/5/1870")
get_details(name="ABC", contact=7123456789, dob="12/5/1870")
