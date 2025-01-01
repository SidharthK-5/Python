"""
Set methods

Properties of sets
Sets are mutable
All the elements should be unique
Immutabe elements in the set - int, float, tuple, str
Unordered
"""

sample_set = {10, 20, 30, 40, 50}
print(f"{sample_set=}")

print("\nadd() method")
sample_set.add(500)
print(f"After adding 500, {sample_set=}")

print("\nunion()")
set_1 = {10, 20, 30, 40, 50, 60}
set_2 = {40, 50, 60, 70, 80, 90}
print(f"{set_1=} \n{set_2=}")
set_3 = set_1.union(set_2)
print(f"Union of set_1 and set_2: {set_3}")

print("\nintersection()")
set_3 = set_1.intersection(set_2)
print(f"Intersection of set_1 and set_2: {set_3}")

print("\ndifference()")
set_3 = set_1.difference(set_2)
print(f"Differece of set_1 and set_2: {set_3}")
set_3 = set_2.difference(set_1)
print(f"Differece of set_2 and set_1: {set_3}")

print(
    "\nsymmetric_difference()"
)  # Gives all elements in the set except the common ones
set_3 = set_1.symmetric_difference(set_2)
print(f"Symmetric difference of set_1 and set_2: {set_3}")

print("\n\nupdate methods")
print(f"{set_1=}\n{set_2=}")
print("\nunion update")
set_1.update(set_2)
print(f"After union update with set_2, {set_1=}")

set_1 = {10, 20, 30, 40, 50, 60}
print("\nintersection_update()")
print(f"{set_1=}")
set_1.intersection_update(set_2)
print(f"After intersecion update with set_2, {set_1=}")

set_1 = {10, 20, 30, 40, 50, 60}
print("\ndifference_update()")
print(f"{set_1=}")
set_1.difference_update(set_2)
print(f"After difference update with set_2, {set_1=}")

set_1 = {10, 20, 30, 40, 50, 60}
print("\nsymmetric_difference_update()")
print(f"{set_1=}")
set_1.symmetric_difference_update(set_2)
print(f"After symmetric difference update with set_2, {set_1=}")

set_1 = {100, 200, 300, 400, 500}
set_2 = {100, 200, 300}
print(f"\n\n{set_1=}\n{set_2=}")

print("\nissubset()")
print(f"Checking is set_2 is a subset of set_1: {set_2.issubset(set_1)}")
print("\nissuperset()")
print(f"Checking if set_1 is a superset of set_2: {set_1.issuperset(set_2)}")

print("\nTypecasting from list to set")
sample_list = [100, 200, 300, 400]
print(f"{set(sample_list)=}")

print("\nCombining two lists without a for loop, using set")
list_1 = [100, 200, 300, 400, 500]
list_2 = [50, 100, 150, 200, 250, 500, 45, 35, 20, 10]
set_1 = set(list_1)
set_2 = set(list_2)
set_3 = set_1.union(set_2)
list_3 = list(set_3)
list_3.sort()
print(f"{list_3=}")

sample_set = {100, 200, 300, 400, 500, 600}
print(f"\n{sample_set=}")
print("\nRandom deletion - pop()")
removed = sample_set.pop()
print(f"Removed {removed} from sample_set")

sample_set = {100, 200, 300, 400, 500, 600}
print("\nselective deletion - remove()")
print(f"{sample_set=}")
sample_set.remove(100)
print(f"After removing 100, {sample_set=}")

sample_set = {100, 200, 300, 400, 500, 600}
print("\nSelective deletion - discard()")
print(f"{sample_set=}")
# Discard won't throw error if the element is absent
sample_set.discard(1000)
print(f"After trying to remove 1000, {sample_set=}")

print("\nclear()")
sample_set.clear()
print(f"sample_set after clear(): {sample_set}")
