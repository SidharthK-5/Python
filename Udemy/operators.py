"""
Types of operators in Python
"""

"""
Identity operator compares the memory loaction of the operands.
So, for immutable datatypes like int and float, same value of different
variables will have same memory location.
Whereas mutable dataypes like list will be stored in different memory locations
even if they hold same values.
"""

num1 = 100
num2 = 100
print(f"{num1=}  {num2=}")

print("\nIdentity operators")
print("Comparing if num1 is the same as num2", end=": ")
print(num1 is num2)

list_1 = [10, 20, 30]
list_2 = [
    10,
    20,
    30,
]  # list_1 and list_2 will not be matched becuase the reference in stack memory is different for both
print(f"\n{list_1=}\n{list_2=}")
print("Comparing if list_1 is the same as list2", end=": ")
print(list_1 is list_2)

print("Comparing if list_1 is not the same as list2", end=": ")
print(list_1 is not list_2)

print("\n\nBitwise operators")
num_1 = 3
num_2 = 4
print(f"{num_1=}  {num_2=}")

print("\nBinary equivalent")
print(
    f"Binary equivalent of {num_1} and {num_2} are {bin(num_1)} and {bin(num_2)} respectively"
)

print("\nBitwise AND (&)")
print(f"{(num_1 & num_2)=}")
print("Bitwise OR (|)")
print(f"{(num_1 | num_2)=}")
print("Left shift 3 << 1")
print(3 << 1)
print("Right shift 3 >> 1")
print(3 >> 1)

print("\nMembership operators (in, not in)\n")
sample_list = [10, 20, 30, 40]
print(f"{sample_list=}")
print(f"Is 30 present in sample_list? {30 in sample_list}")
print(f"Is 50 not present in sample_list?{50 not in sample_list}")

string = "Python"
print(f"\n{string=}")
print(f"Is 'p' present in string? {'p' in string}")
print(f"Is 'P' present in string? {'P' in string}")
