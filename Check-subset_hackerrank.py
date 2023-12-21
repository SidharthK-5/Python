T = int(input()) #No of test cases
while T>0:
    a = int(input())
    A = set(map(int, input().split())) #Subset
    b = int(input())
    B = set(map(int, input().split())) #Superset

    if A.issubset(B):
        print(True)
    else:
        print(False)
    
    T -= 1
