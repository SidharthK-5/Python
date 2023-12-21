'''
We can use the following operations to create mutations to a set:

.update() or |=
Update the set by adding elements from an iterable/another set.

.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

.difference_update() or -=
Update the set by removing elements found in an iterable/another set.

.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.

'''
a = int(input())
A = set(map(int, input().split()))
N = int(input())
op_list = []

for i in range(N):
    r = input().split()
    s = set(map(int, input().split()))
    r.append(s)
    op_list.append(r)

for i in range(N):
    if op_list[i][0] == 'intersection_update':
        A.intersection_update(op_list[i][2])
    elif op_list[i][0] == 'update':
        A.update(op_list[i][2])
    elif op_list[i][0] == 'symmetric_difference_update':
        A.symmetric_difference_update(op_list[i][2])
    elif op_list[i][0] == 'difference_update':
        A.difference_update(op_list[i][2])
    
print(sum(A))