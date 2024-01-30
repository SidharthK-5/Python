"""
Demo of some common math functions
"""

import math

# fsum - print float sum of a list
float_list = [0.1] * 10
print(f"{float_list=}")
print(f"fsum of list float_list is: {math.fsum(float_list)}")

# upper and lower bound
print("\nfloor and ceil of 15.999 are:", math.floor(15.5559), math.ceil(15.5559))

# Factorial
print(f"\nFactorial of 5 is = {math.factorial(5)}")

# modf function - seperates int and decimal part
# Returns a tuple (dec,int)
print(f"\nFractional and decimal parts of 45.556 are: {math.modf(45.5556)}")  # method 1
fractional, integer = map(float, math.modf(45.556))  # method 2
print(f"Parts separated: {integer=}, {fractional=}")

# log function
print("\nLogarithmic functions")
print(f"log of 10 to the base 3 = {math.log(10, 3)}")  # log of 10 to the base 3
print(f"Natural log of 10 = {math.log(10)}")  # natural logarithm
print(f"Common log of 100 = {math.log10(100)}")  # common log
print(f"Log of 10 to the base 2 = {math.log2(10)}")

# deg to rad
print("\nConverting degree to radian")
print(f"30 degree in radian = {math.radians(30)}")
