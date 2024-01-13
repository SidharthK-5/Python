from itertools import count


n = int(input())
A = []
for i in range(n):
    r = input()
    A.append(r)

dict = {}
for i in A:
    dict[i] = A.count(i)

print(len(dict))
for key in dict:
    print(dict[key], end=" ")
