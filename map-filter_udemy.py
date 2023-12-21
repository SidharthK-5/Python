def sq(n):
    return n**2

def add(n1,n2):
    return n1+n2

def M20(n):
    if n%20 == 0:
        return True
    else:
        return False

# map()
l = [10,20,30,40,50]
l1 = list(map(sq, l))
print(l1)

l2 = list(map(add, l, l1))
print(l2)

# filter()
l3 = list(filter(M20, l))
print(l3)