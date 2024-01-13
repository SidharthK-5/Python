"""
Decorators take function as argument and returns a function
"""


def deco(func):
    def new_fun(val1, val2):
        if type(val1) == type(val2):
            return func(val1, val2)
        else:
            return func(str(val1), str(val2))

    return new_fun


@deco
def concat(val1, val2):
    return val1 + val2


result = concat(10, 10)
print(result)

result = concat("Python", 10)
print(result)

result = concat("Python", "String")
print(result)
