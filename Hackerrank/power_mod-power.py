"""
Question:
Given 3 numbers: a, b and m in 3 lines
Print the result as follows:
1st line should be a^b
2nd line should be a^b % m
"""

a = int(input())
b = int(input())
m = int(input())

print(pow(a, b))
print(pow(a, b, m))  # mod-power
