"""
Question:
Given a large set and some other sets. Check if the large set is the strict superset of all the other sets
Print True if large set is the strict superset of all the others and False otherwise
"""

large_set = set(map(int, input().split()))  # Superset
num_cases = int(input())  # no of test cases
list_of_sets = []  # list of subsets
for case in range(num_cases):
    # Entering subsets row by row
    small_set = set(map(int, input().split()))
    list_of_sets.append(small_set)

flag = 1  # Initialising flag = 1 assuming large_set is a strict superset of all
for case in range(num_cases):
    if large_set.issuperset(list_of_sets[case]) and len(large_set) > len(
        list_of_sets[case]
    ):
        # For strict superset, there will be atleast one element extra comparing to subset
        continue
    else:
        flag = 0
        break

if flag:
    print(True)
else:
    print(False)
