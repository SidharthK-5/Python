X = int(input()) # No of shoes
shoes = input().split(" ") # diff sizes of shoes available
N = int(input()) # No of customers waiting
need_list = [] # list to store user needs
total = 0
for i in range(N):
    # Loop taking user inputs line by line
    r = input().split(" ")
    need_list.append(r)

for i in range(N):
    a = need_list[i][0]
    if a in shoes:
        # if required shoe size is present, add price. Else pass
        total += int(need_list[i][1])
        shoes.remove(a)
    else:
        pass

print(total)