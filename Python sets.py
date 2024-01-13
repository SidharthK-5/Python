print("Python Sets")

# Sets are mutable
# All the elements should be unique
# Immutabe elements in the set - int, float, tuple, str
# Unordered

s = {10, 20, 30, 40, 50}
print(s)

print("add()")
s.add(500)
print(s)

print("\nunion()")
s1 = {10, 20, 30, 40, 50, 60}
s2 = {40, 50, 60, 70, 80, 90}
print(s1, "\n", s2)
s3 = s1.union(s2)
print(s3)

print("\nintersection()")
s3 = s1.intersection(s2)
print(s3)

print("\ndifference()")
s3 = s1.difference(s2)
print(s3)
s3 = s2.difference(s1)
print(s3)

print(
    "\nsymmetric_difference()"
)  # Gives all elements in the set except the common ones
s3 = s1.symmetric_difference(s2)
print(s3)

print("\nupdate methods")
print("union update")
s1.update(s2)
print(s1)

s1 = {10, 20, 30, 40, 50, 60}
print("\nintersection_update()")
s1.intersection_update(s2)
print(s1)

s1 = {10, 20, 30, 40, 50, 60}
print("\ndifference_update()")
s1.difference_update(s2)
print(s1)

s1 = {10, 20, 30, 40, 50, 60}
print("\nsymmetric_difference_update()")
s1.symmetric_difference_update(s2)
print(s1)

s1 = {100, 200, 300, 400, 500}
s2 = {100, 200, 300}
print(s1, "\n", s2)
print("\nissubset()")
print(s2.issubset(s1))
print("\nissuperset()")
print(s1.issuperset(s2))

print("\nTypecasting from list to set")
l = [100, 200, 300, 400]
print(s)

print("\nCombining two lists without a for loop, using set")
l1 = [100, 200, 300, 400, 500]
l2 = [50, 100, 150, 200, 250, 500, 45, 35, 20, 10]
s1 = set(l1)
s2 = set(l2)
s3 = s1.union(s2)
l3 = list(s3)
l3.sort()
print(l3)

s = {100, 200, 300, 400, 500, 600}
print("\nRandom deletion - pop()")
r = s.pop()
print(s, r)

s = {100, 200, 300, 400, 500, 600}
print("\nselective deletion - remove()")
s.remove(100)
print(s)

s = {100, 200, 300, 400, 500, 600}
print("\nSelective deletion - discard()")
# Discard won't throw error if the element is absent
s.discard(1000)
print(s)

print("\nclear()")
s.clear()
print(s)
