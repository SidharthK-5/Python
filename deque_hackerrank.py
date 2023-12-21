# Program to show deque type
from collections import deque
d = deque()

def do_operation(A):
    if A[0] == "append":
        d.append(A[1])
    elif A[0] == "appendleft":
        d.appendleft(A[1])
    elif A[0] == "pop":
        d.pop()
    elif A[0] == "popleft":
        d.popleft()
    elif A[0] == "rotate":
        d.rotate(A[1])
    elif A[0] == "extend":
        d.extend(A[1])
    elif A[0] == "extendleft":
        d.extendleft(A[1])
    elif A[0] == "reverse":
        d.reverse()
    

N = int(input())
for i in range(N):
    r = input().split(' ')
    do_operation(r)

for i in range(len(d)):
    print(d[i], end = " ")
