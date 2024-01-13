l = [10, 15, 20, 25, 30, 35]

# Square list
l1 = [i * i for i in l]
print(l1)

# Even no list
l1 = [i for i in l if i % 2 == 0]
print(l1)

# Length of item list
l = ["abc", "abcd", "abcabc"]
l1 = [len(i) for i in l]
print(l1)

# Nested for loops in comprehension
l = [(i, j) for i in range(1, 5) for j in range(100, 102)]
print(l)

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l1 = [j for i in l for j in i]
print(l1)

# Multiple output specification
l = [10, 15, 20, 25, 30, 35]
l1 = ["Even" if i % 2 == 0 else "Odd" for i in l]
print(l1)

print("\nCombining two lists based on condition")
a = [1, 2, 3, 4]
b = ["a", "b", "c", "d"]
li = [[i, j] for i in a for j in b if a.index(i) == b.index(j)]
print(li)

print(list(zip(a, b)))  # Creates tuples by combining elements from a and b
li2 = [list(i) for i in zip(a, b)]
print(li2)

print("\nComprehension based on type of element")
x = ["P", 5, 1, "Q", "r", 6]
st = [i for i in x if type(i) == str]
print(st)

print("\nList comprehension to create generator object")
# Instead of [] in comprehension, put ()
# Generator object doesn't create new list, but it generates an iterable object
# This saves memory space with the same utility
s = (i for i in range(101) if i % 5 == 0)
print(s)
print(list(s))
