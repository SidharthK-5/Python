print("Dictionary creation with two lists")

l1 = [1, 2, 3, 4, 5]
l2 = [1, 4, 9, 16, 25]

d = dict(zip(l1, l2))
print(d)

print("Dictionary from one list")
print("Using fromkeys()")

l = [1, 2, 3, 4, 5]
d1 = dict.fromkeys(l, 0)
print(d1)

print("Merging two dictionaries")

d2 = {1: 1, 2: 4, 3: 9}
d3 = {4: 16, 5: 25}
d2.update(d3)
print(d2)

print("pop()")
r = d2.pop(5)
print(d2, r)

print("popitem()")
r = d2.popitem()
print(d2, r)

print("clear()")
d2.clear()
print(d2)

print("del method")
del d2
