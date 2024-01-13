"""
Adding elements to a set
"""

N = int(input())  # No of elements to add
x = set()
for i in range(N):
    # Add inputs to a set
    s = input()
    x.add(s)

print(len(x))
