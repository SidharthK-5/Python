print("Identity operators")

"""Identity operator compares the memory loaction of the operands.
So, for immutable datatypes like int and float, same value of different
variables will have same memory location.
Whereas mutable dataypes like list will be stored in different memory locations
even if they hold same values."""

num1 = 100
num2 = 100
print(num1 is num2)

l1 = [10, 20, 30]
l2 = [10, 20, 30]
print(l1 is l2)

print(l1 is not l2)

print("\nBitwise operators\n")
n1 = 3
n2 = 4

print("Binary equivalent")
print("Binary equivalent of 3 and 4 are respectively", bin(n1), bin(n2))

print("Bitwise AND (&)")
print(n1 & n2)
print("Bitwise OR (|)")
print(n1 | n2)
print("Left shift 3 << 1")
print(3 << 1)
print("Right shift 3 >> 1")
print(3 >> 1)

print("\nMembership operators (in, not in)\n")
l = [10, 20, 30, 40]
print(30 in l)
print(50 not in l)
s = "Python"
print("p" in s)
print("P" in s)
