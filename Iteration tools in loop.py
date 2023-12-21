# break continue pass enumerate

l = [10,20,30,40,50,60]
key = 40

for value in l:
    if  value == key:
        print("Element found")
        break
    else:
        continue

else:
    # else for a for loop
    print("Element not found")

print("Enumerate fn")

for index,value in enumerate(l):
    # Prints index and value at index
    #print(index, value)

    if  value == key:
        print("Element found at index", index)
        break
    else:
        continue

print("pass keyword")

''' pass is actually used for doing nothing. When a particular block is blank,
it will throw an error, in order to avoid this, pass can be used. Usually, we
write nothing in that block where pass is used'''

for index,value in enumerate(l):
    if  value == key:
        print("Element found at index", index)
        break
    else:
        pass
        print("Statement after pass")
        
