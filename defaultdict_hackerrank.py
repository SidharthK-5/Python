""" Question: Given 2 nos, n and m, the no of elements in lists A and B respectively
              If an element in B is present in A, print the position of that element in A
              Else, print -1"""

from collections import defaultdict

d = defaultdict(list) # This defaultdict will store lists A and B
n, m = map(int, input().split())

for _ in range(n):
    d['A'].append(input()) # Elements of key A
for _ in range(m):
    d['B'].append(input()) # Elements of key A

for i in d['B']: # To check for every element in B
    flag = 0
    for j in range(len(d['A'])):
        if d['A'][j] == i: # Match is found, position is printed
            flag = 1
            print(j+1, end=' ')
    
    if flag == 0: # When the particular 'i' is not found in key A
        print(-1, end=' ')
    print()
