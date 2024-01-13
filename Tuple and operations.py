""" Tuple and operations """
t = (10, 20, 30, 40)
print(t, type(t))

print("Operations\nSame as that of list, but cannot edit the tuple\n")
print("enumerate() given below for the list actually returns a tuple of (index, value)")
l = [10, 20, 30, 40]
print(l)
for i in enumerate(l):
    print(i)
