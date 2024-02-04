"""
Quesstion:
Given one list N and two disjoint sets A & B
Your initial 'happiness' is 0.
For each element in A, happiness increases by 1 and for each element in B, happiness decreases by 1
Find the total happiness
"""

n, m = map(
    int, input().split()
)  # n = No. of elements in list N, m = No. of elements in sets
N = list(map(int, input().split()))  # list of n elements
# A & B are disjoint sets with m elements each
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0

for i in range(n):
    if N[i] in A:
        happiness += 1
    elif N[i] in B:
        happiness -= 1

print(happiness)
