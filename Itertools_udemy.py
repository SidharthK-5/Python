import itertools

# Simple iter demo - no need of itertools
l = [10, 20, 30, 40]
i = iter(l)
for val in i:
    print(val, end=" ")
print("\n")

# Itertools chain method
l1 = [100, 200, 300, 400]
l2 = [1000, 2000, 3000, 4000]
i = itertools.chain(l, l1, l2)
for val in i:
    print(val, end=" ")
print("\n")

# Itertools cycle - for cyclic iteration
count = 0
for val in itertools.cycle(l):
    if count < 20:
        print(val, end=" ")
    else:
        break
    count += 1
print("\n")

# Itertools repeat - for repeated iteration of same val
count = 0
for val in itertools.repeat(l):
    if count < 5:
        print(val, end=" ")
    else:
        break
    count += 1
print("\n")

# Itertools tee - cycling iteration
i = iter(l)
t = itertools.tee(i, 5)
for j in range(5):
    for val in t[j]:
        print(val, end=" ")
print("\n")

# Itertools islice method for slicing chain
i = itertools.chain(l, l1, l2)
for val in itertools.islice(i, 0, 6):
    print(val, end=" ")

print("\n")

# count() for infinite value generation
count = 0
for val in itertools.count(
    10, 5
):  # We can only specify start and step, but not end. It is defined using counter
    if count > 10:
        break
    else:
        print(val, end=" ")
    count += 1
print("\n")

# Permutations and combinations
l = [1, 2, 3]
print(
    list(itertools.permutations(l, 2))
)  # parameters: list and no of items for combination/permutaion
print(list(itertools.combinations(l, 2)))
