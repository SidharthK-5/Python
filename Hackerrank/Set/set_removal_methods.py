"""
Question: Given a main set an a set of removal operations
Perform these operations on main set with the corresponding number
"""

num_elements = int(input())
main_set = set(map(int, input().split()))
num_cases = int(input())
operations_list = []

for _ in range(num_cases):
    # e = input().split(" ")
    # op_list.append(e)
    operations_list.append(input().split())

# Perform operations case by case
for case in range(num_cases):
    if operations_list[case][0] == "pop":
        main_set.pop()
    elif operations_list[case][0] == "remove":
        main_set.remove(int(operations_list[case][1]))
    elif operations_list[case][0] == "discard":
        main_set.discard(int(operations_list[case][1]))

# Sum of remaining elements in main set
print(sum(main_set))
