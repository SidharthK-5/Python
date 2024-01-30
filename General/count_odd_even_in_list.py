"""
Input a list of integers. Return the count even numbers and odd numbers
"""

numbers = input().split()
odd_sum = 0
even_sum = 0
for number in numbers:
    if int(number) % 2 == 0:
        even_sum += 1
    else:
        odd_sum += 1

print(f"\nCount of even numbers: {even_sum}")
print(f"Count of odd numbers: {odd_sum}")
