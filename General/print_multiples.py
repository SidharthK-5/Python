"""
Print numbers which are divisible by 5 and 7 in the range 1500 and 2700
"""

for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)
