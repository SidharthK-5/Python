"""
Find the symmetric difference of two sets and
print the difference set in ascending order.
"""

N = int(input())
set_N = set(map(int, input().split()))
M = int(input())
set_M = set(map(int, input().split()))

print(*sorted(set_N.symmetric_difference(set_M)), sep="\n")
