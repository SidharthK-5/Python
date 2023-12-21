def move_zeros(l):
    count = 0
    while 0 in l:
        l.remove(0)
        count += 1
    l.extend([0]*count)
    return l
        
# Read the variable from STDIN
a = int(input())
l = []
for i in range(a):
    l.append(int(input()))

a = move_zeros(l)

# Output the variable to STDOUT
print(a)
