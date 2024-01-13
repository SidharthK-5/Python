""" Question: Sort a string S using following coditions
                All sorted lowercase letters are ahead of uppercase letters.
                All sorted uppercase letters are ahead of digits.
                All sorted odd digits are ahead of sorted even digits.
        Eg: Sorting1234 to ginortS1324 """


S = input()
ginortS = []
small = []
caps = []
odd = []
even = []

for i in S:
    if ord(i) in range(97, 123):
        small.append(i)
    elif ord(i) in range(65, 91):
        caps.append(i)
    elif ord(i) in range(48, 58):
        if ord(i) % 2 == 1:
            odd.append(i)
        else:
            even.append(i)

ginortS = sorted(small) + sorted(caps) + sorted(odd) + sorted(even)
print("".join(ginortS))
