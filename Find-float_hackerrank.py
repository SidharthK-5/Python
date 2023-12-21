import re
T = int(input())
for i in range(T):
    n = input()
    print(bool(re.search("^[+-]?\d*\.\d+$",n)))
