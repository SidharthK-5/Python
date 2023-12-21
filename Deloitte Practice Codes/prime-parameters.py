def isPrime(num):
    if num<2 or num>1000:
        return "Out of Range"
    else:
        flag = 0
        for n in range(2, num//2 + 1):
            if num % n == 0:
                flag = 1
                break
        if flag == 1:
            return "COMPOSITE"
        else:
            return "PRIME"

# Read the variable from STDIN
T = int(input())
L = list()
for i in range(T):
    L.append(int(input()))

# Output the variable to STDOUT
for num in L:
    ret = isPrime(num)
    print(ret)
