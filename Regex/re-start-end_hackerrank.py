"""
Question:
Given two strings S and k
Find the indices of the start and end of string k in S
(This has to be implemented with re.start() and re.end(). Couldn't find a way to do so)
"""

S = input()
k = input()
pattern_length = len(k)

i = 0
flag = 0
while i < len(S):
    if k == S[i : i + pattern_length]:
        flag = 1
        print((i, i + pattern_length - 1))
    i += 1

if flag == 0:
    print((-1, -1))
