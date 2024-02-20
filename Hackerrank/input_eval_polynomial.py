"""
Question:
Given two values x and k
Polynomial P contains algebraic expressions using variable as x
Evaluate the polynomial
If value of P = k, print True, else False
"""

x, k = map(int, input().split())
P = input()
if eval(P) == k:
    print(True)
else:
    print(False)
