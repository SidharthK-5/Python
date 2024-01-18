"""
Generator function are used if the function creates a large series of nos.
'yield' will stop the multiple times execution
exectues only once and wait for the next call of next(). This saves memory
"""


# Fibonacci using generator
def generate_fibonacci_num():
    """
    Generates Fibonacci numbers using python generator

    Yields:
        int: The subsequent Fibonacci number
    """
    first = 0
    yield first
    second = 1
    yield second
    while True:
        next = first + second
        yield next
        first, second = second, next


print("Fibonacci series with Generator function")
fibo_generator = generate_fibonacci_num()
for _ in range(10):
    print(next(fibo_generator))

print("\nList comprehension and Generator function")
# Generator concept in comprehension
list_1 = [10, 20, 30, 40, 50]
list_2 = (
    value**2 for value in list_1
)  # Giving () instead of [] in comprehension will create a generator object list_2
for _ in range(len(list_1)):
    print(next(list_2))
