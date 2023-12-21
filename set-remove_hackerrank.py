n = int(input())
s = set(map(int, input().split()))
N = int(input())
op_list = []

for i in range(N):
    e = input().split(' ')
    op_list.append(e)

for i in range(N):
    if op_list[i][0] == 'pop':
        s.pop()
    elif op_list[i][0] == 'remove':
        s.remove(int(op_list[i][1]))
    elif op_list[i][0] == 'discard':
        s.discard(int(op_list[i][1]))

print(sum(s))
