# Variable length argument function

import email
from unicodedata import name


def add_value(*args):
    l = []
    for i in args:
        l.append(i)
    return l


result = add_value(100, 200, 300, 400, 500)
print(result)
result = add_value(
    100,
    200,
)
print(result)
result = add_value(100, 200, 300, 400, 500, 600, 700, 800)
print(result)

print("\n\n")
# Variable length keyword argument fn


def get_details(**kwargs):
    print(kwargs)


get_details(name="ABC", email="abc@gmail.com", contact=7123456789, dob="12/5/1870")
get_details(name="ABC", email="abc@gmail.com", dob="12/5/1870")
get_details(name="ABC", contact=7123456789, dob="12/5/1870")
