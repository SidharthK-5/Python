"""
List operations in Python
"""

print("\nList operations\n")

sample_list = [10, 20, 30, 40, "Python", "Java", [100, 200, 300]]
print(f"{sample_list=}")

print(f"\nSlicing on sample_list: {sample_list[4:6]=}")  # Slicing
print(f"Striding with reversal: {sample_list[::-1]=}")  # Striding for reversal

print("\nPrinting alternate elements with striding")
for iterator in sample_list[::2]:
    print(iterator, end=" ")

list_1 = [100, 200, 300, 400, 500]
print(f"\n{list_1=}")

print("\nappend() method:")
list_1.append(600)
print(f"After appending 600, {list_1=}")

print(
    "\nAdd multiple elements using extend() method : "
)  # Add multiple elements to a list
list_1.extend([700, 800, 900])  # l1 + [700, 800, 900] will work the same
print(f"After adding [700, 800, 900]: {list_1=}")

print("\nDifference b/w append and extend")
list_1.append("Python")
print(f"After appending 'Python', {list_1=}")
list_1.extend("Python")
print(f"After entending 'Python', {list_1=}")

print("\ninsert() method:")
list_1.insert(1, 150)
print(f"After inserting 150 at index 1, {list_1=}")

""" The best method to copy a list to another is by using copy(). Else, while
changing the original list, both lists will get changed because list is mutable"""

print("\nList .copy()")
list_a = [10, 20, 30]
list_a1 = list_a.copy()
print(f"{list_a=}, {id(list_a)=}, {list_a1=}, {id(list_a1)=}")
list_a.append(40)
print(
    f"After appending 40 to list_a:\n{list_a=}, {id(list_a)=}, {list_a1=}, {id(list_a1)=}"
)

print("\nupdate method:")
list_b = [10, 20, 300, 40, 50]
print(f"{list_b=}")
list_b[2] = 30
print(f"After updating 2nd index of list_b, {list_b=}")

print("\nChanging multiple elements of a list")
list_b[0:2] = [15, 25]
print(f"After updating 0th and 1st indices, {list_b=}")

print("\nElement removal methods:")
print("pop() - Removal based on index")
removed = list_b.pop(4)
print(f"Updated {list_b=}, popped element: {removed}")
print("\nremove() - Removal based on value")
list_b.remove(25)
print(f"After removing 25, {list_b=}")

print("\ndel - Deletes the address of the list: del [list_name]")
print("del can also be used to remove multiple elements:")
del list_b[0:2]
print(f"Updated after deleting first two elements: {list_b=}")

print("\nclear() - Removes all elements from the list")
list_b.clear()
print(f"After clear(), {list_b=}")

print("\nSorting methods")
list_c = [50, 30, 40, 20, 10]
print(f"{list_c=}")
list_c.sort()
print(f"Sorted {list_c=}")

"""
sorted(c) => same as c.sort()
revesal => c[::-1] or c.reverse() or c.sort(reverse = True)
"""

print("\nindex() and count()")
list_d = [10, 20, 30, 30, 40]
print(f"{list_d=}")
print("index of 30:", list_d.index(30))
print("count of 30:", list_d.count(30))
