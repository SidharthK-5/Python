"""
Within the limit check for multiples of 3 and 5
- Multiple of 3 -> Print "fizz"
- Multiple of 5 -> Print "buzz"
- Multiple of both 3 and 5 -> Print "fizzbuzz"
- Else, print the number
"""

limit = int(input())
for num in range(1, limit + 1):
    if num % 15 == 0:
        print("fizzbuzz")
    else:
        if num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)
