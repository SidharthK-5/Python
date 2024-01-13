n, m = map(int, input().split())
N = list(map(int, input().split()))  # list of n elements
# A & B are disjoint sets with m elements each
A = set(map(int, input().split()))
B = set(map(int, input().split()))
Happiness = 0

for i in range(n):
    if N[i] in A:
        Happiness += 1
    elif N[i] in B:
        Happiness -= 1

print(Happiness)
