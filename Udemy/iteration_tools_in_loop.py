"""
Control statements and enumerate function in loops
"""

sample_list = [10, 20, 30, 40, 50, 60]
print(f"{sample_list=}")
search_value = 40

# break continue pass enumerate
print("\nbreak and continue statements")
for value in sample_list:
    if value == search_value:
        print(f"{search_value} found in sample_list...\nBreaking the loop")
        break
    else:
        continue  # Skip the current iteration and move to the next value

else:
    # else for a for loop
    print(f"{search_value} not present in sample_list")

print("\nEnumerate function")
for index, value in enumerate(sample_list):
    # Prints index and value at index
    # print(index, value)

    if value == search_value:
        print(f"{search_value} found at index {index}...\nBreaking the loop")
        break
    else:
        continue

print("\npass keyword")
"""
pass is actually used for doing nothing. When a particular block is blank,
it will throw an error, in order to avoid this, pass can be used. Usually, we
write nothing in that block where pass is used
"""

for index, value in enumerate(sample_list):
    if value == search_value:
        print(f"{search_value} found at index {index}...\nBreaking the loop")
        break
    else:
        pass
        print("Statement after pass")
