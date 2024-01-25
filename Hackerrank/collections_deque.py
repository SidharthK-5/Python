"""
deque is a double ended queue

Question:
Given some operations and values separated by a space. Perform these operation on deque
Return the space separated elements in the deque
"""

from collections import deque

dictionary = deque()


def do_operation(A):
    if A[0] == "append":
        dictionary.append(A[1])
    elif A[0] == "appendleft":
        dictionary.appendleft(A[1])
    elif A[0] == "pop":
        dictionary.pop()
    elif A[0] == "popleft":
        dictionary.popleft()
    elif A[0] == "rotate":
        dictionary.rotate(A[1])
    elif A[0] == "extend":
        dictionary.extend(A[1])
    elif A[0] == "extendleft":
        dictionary.extendleft(A[1])
    elif A[0] == "reverse":
        dictionary.reverse()


N = int(input())
for inp in range(N):
    row = input().split(" ")
    do_operation(row)

for key in range(len(dictionary)):
    print(dictionary[key], end=" ")
