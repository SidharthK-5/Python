# K = int(input())
# room_nos = sorted(list(map(int, input().split())))
# s = set(room_nos)
# s1 = list(s)

# for i in range(len(s1)):
#   room_nos.remove(s1[i])

# room_nos = set(room_nos)
# print(sum(s.difference(room_nos)))

# K = int(input())
# room_nos = sorted(list(map(int, input().split())))

# for i in range(0, len(room_nos), K):
#     if i+K > len(room_nos):
#         print(room_nos[i])
#     elif room_nos[i] == room_nos[i+K-1]:
#         continue
#     else:
#         print(room_nos[i])
    


# K = int(input())
# room_nos = sorted(list(map(int, input().split())))

# for i in range(0, len(room_nos), K):
#     c = room_nos[i]
#     if room_nos.count(c) == 1:
#         print(c)

N = int(input())

storage = map(int, input().split())
storage = sorted(storage)

for i in range(len(storage)):
    if(i != len(storage)-1):
        if(storage[i]!=storage[i-1] and storage[i]!=storage[i+1]):
            print(storage[i])
            break
    else:
        print(storage[i])