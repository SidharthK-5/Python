"""
Tuple and operations
Tuple operations are same as that of list, but tuples cannot be edited
"""

sample_tuple = (10, 20, 30, 40)
print(f"{sample_tuple=} {type(sample_tuple)=}\n")

# enumerate() given below for the list actually returns a tuple of (index, value)
demo_list = [10, 20, 30, 40]
print(f"{demo_list=}")
for item in enumerate(demo_list):
    print(item)
