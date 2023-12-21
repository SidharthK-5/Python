A = set(map(int, input().split())) #Superset
n = int(input()) # no of test cases
S = [] # list of subsets
for i in range(n):
    #Entering subsets row by row
    r = set(map(int, input().split()))
    S.append(r)

flag = 1
for i in range(n):
    if A.issuperset(S[i]) and len(A) > len(S[i]):
        # For strict superset, there will be atleast one element extra comparing to subset
        continue
    else:
        flag = 0
        break

if(flag == 1):
    print(True)
else:
    print(False)