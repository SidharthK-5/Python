import math

# fsum - print float sum of a list
l = [0.1] * 10
print(l)
print("fsum of list l is : ", math.fsum(l))

# upper and lower bound
print("floor and ceil of 15.999 are : ", math.floor(15.5559), math.ceil(15.5559))

# Factorial
print(math.factorial(5))

# modf function - seperates int and decimal part
# Returns a tuple (dec,int)
print(math.modf(45.5556))  # method 1
d, i = map(float, math.modf(45.556))  # method 2
print(d, i)

# log function
print(math.log(10, 3))  # log of 10 to the base 3
print(math.log(10))  # natural logarithm
print(math.log10(100))  # common log
print(math.log2(10))

# deg to rad
print(math.radians(30))
