"""
We can use the following operations to create mutations to a set:

.update() or |=
Update the set by adding elements from an iterable/another set.

.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

.difference_update() or -=
Update the set by removing elements found in an iterable/another set.

.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.

---------------------------------------------------------------------------------------------

Question: Given a main set and number of sets and a corresponding operations
for each set, perform it's corresponding mutation operation on the main set
"""

# Input main set and number of test cases
num_elements_main_set = int(input())
main_set = set(map(int, input().split()))
num_cases = int(input())
operations_list = []

# Make a list of mutations
for _ in range(num_cases):
    # row contains mutation, num_elements
    row = input().split()
    # set entry corresponds to row mutation
    set_entry = set(map(int, input().split()))
    row.append(set_entry)
    operations_list.append(row)

# For each set, perform mutation on the main set
for case_id in range(num_cases):
    if operations_list[case_id][0] == "intersection_update":
        main_set.intersection_update(operations_list[case_id][2])
    elif operations_list[case_id][0] == "update":
        main_set.update(operations_list[case_id][2])
    elif operations_list[case_id][0] == "symmetric_difference_update":
        main_set.symmetric_difference_update(operations_list[case_id][2])
    elif operations_list[case_id][0] == "difference_update":
        main_set.difference_update(operations_list[case_id][2])

# Sum of remaining elements in main set
print(sum(main_set))
