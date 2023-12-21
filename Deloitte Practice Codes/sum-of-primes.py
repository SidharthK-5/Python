def sumprimes(ls):
    a = 0
    for i in ls:
        if i > 1:
            flag = 0
            for j in range(2, (i // 2) + 1):
                if i%j == 0:
                    flag = 1
                    break
            if flag == 0:
                a += i
    
    return a

# Read the variable from STDIN
ls = list(map(int, input().split()))
a = sumprimes(ls)
# Output the variable to STDOUT
print(a)
