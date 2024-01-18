# map()
l = [10, 20, 30, 40, 50]
l1 = list(
    map(lambda n: n ** 2, l)
)  # This lambda calculates square of every element from 'l'
print(l1)

l2 = list(map(lambda n1, n2: n1 + n2, l, l1))  # n1 is taken from l, n2 is taken from l1
print(l2)

# filter()
l3 = list(
    filter(lambda n: n % 20 == 0, l)
)  # Filters the values from 'l', which satisfies the given lambda (multiples of 20)
print(l3)

# Dict sorting based on values
d = {8: 50, 3: 40, 2: 30, 1: 20, 5: 10}
l = dict(
    sorted(d.items(), key=lambda x: x[1])
)  # key will take the lambda fn and lambda inputs a tuple (d.items()) and returns x[1] or value in tuple. This key is used by sorted()
print(l)
