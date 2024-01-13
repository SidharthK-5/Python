import re

S = input()
k = input()
ln = len(k)

i = 0
flag = 0
while i < len(S):
    if k == S[i : i + ln]:
        flag = 1
        print((i, i + ln - 1))
    i += 1

if flag == 0:
    print((-1, -1))
