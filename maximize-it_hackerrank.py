k, m = map(int, input().split())
lists = []
mods = []
for _ in range(k):
    r = list(map(int, input().split()))
    lists.append(r[1:])

for i in range(len(lists)):
    for j in range(len(lists[i])):
        lists[i][j] = (lists[i][j]**2) % m

S = 0    
for l in lists:
    S += max(l)

print(S)