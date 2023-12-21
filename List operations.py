''' List operations '''

l = [10,20,30,40,"Python","Java",[100,200,300]]
print(l)

print(l[4:6]) # Slicing
print(l[::-1]) # Striding for reversal

print("\nPrinting alternate elements")
l1 = [100,200,300,400,500]
for i in l[::2]:
    print(i)

print("\nappend() method : ")
print(l1)
l1.append(600)
print(l1)

print("\nextend() method : ") # Add multiple elements to a list
l1.extend([700,800,900]) # l1 + [700, 800, 900] will work the same
print(l1)

print("\nDifference b/w append and extend")
l1.append("Python")
print("append() :",l1)
l1.extend("Python")
print("extend() :",l1)

print("\ninsert() method :")
l1.insert(1,150)
print(l1)

''' The best method to copy a list to another is by using copy(). Else, while
changing the original list, both lists will get changed because list is mutable'''

a = [10,20,30]
a1 = a.copy()
a.append(40)
print(a,id(a),a1,id(a1))

print("\nupdate method :")
b = [10,20,300,40,50]
print(b)
b[2] = 30
print(b)
print("\nChanging multiple elements of a list")
b[0:2] = [15, 25]
print(b)

print("\nElement removal methods :")
print("pop() - Removal based on index")
r = b.pop(4)
print(b,r)
print("remove() - Removal based on value")
b.remove(25)
print(b)
print("del - Deletes the address of the list : del [list_name]")
print("del can also be used to remove multiple elements:")
del(b[0:2])
print(b)

print("clear() - Removes all elements from the list")
b.clear()
print(b)

print("\nSorting methods")
c = [50,30,40,20,10]
c.sort()
print("sort() :",c)
'''
sorted(c) => same as c.sort()
revesal => c[::-1] or c.reverse() or c.sort(reverse = True) '''

print("index() and count()")
d = [10,20,30,30,40]
print(d)
print("index of 30 :",d.index(30))
print("count of 30 :",d.count(30))