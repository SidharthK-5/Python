"""
Question:
Given 2 nos, n and m, the no of elements in lists A and B respectively
For each element in B, check if it is present in A
If present, print the position of that element in A
Else, print -1
"""

from collections import defaultdict

d = defaultdict(list)  # This defaultdict will store lists A and B
n, m = map(int, input().split())  # n -> no. of elements in A, m -> no. of elements in B

for _ in range(n):
    d["A"].append(input())  # Elements of key A
for _ in range(m):
    d["B"].append(input())  # Elements of key A

for item_in_B in d["B"]:  # To check for every element in B
    flag = 0
    for idx_in_A in range(len(d["A"])):
        if d["A"][idx_in_A] == item_in_B:  # Match is found, print the position
            flag = 1
            print(idx_in_A + 1, end=" ")

    if flag == 0:  # When the particular 'item_in_B' is not found in key A
        print(-1, end=" ")
    print()
