import re

num = "^[7-9][0-9]{9}$"
N = int(input())
A = []
for i in range(N):
    r = input()
    A.append(r)

for i in A:
    if re.match(num, i):
        print("YES")
    else:
        print("NO")
