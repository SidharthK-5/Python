"""
Question: User enters number of test cases
For each case, user will input two sets
Task is to check if 1st set is the subset of 2nd set
"""

num_cases = int(input())  # No of test cases
while num_cases > 0:
    num_elements_set_1 = int(input())
    set_1 = set(map(int, input().split()))  # Subset
    num_elements_superset = int(input())
    superset = set(map(int, input().split()))  # Superset

    if set_1.issubset(superset):
        print(True)
    else:
        print(False)

    num_cases -= 1
