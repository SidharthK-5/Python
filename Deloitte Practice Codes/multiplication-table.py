# Read the variable from STDIN
T = int(input())
L = list()
for i in range(T):
    L.append(int(input()))

# Output the variable to STDOUT
for num in L:
    for i in range(1,11):
        print("{} x {} = {}".format(num, i, num*i))
    print("===============")
