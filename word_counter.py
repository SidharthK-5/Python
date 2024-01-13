# Words counter


def counter(s):
    c = 1
    for i in s:
        if i == " ":
            c += 1

    return c


s = input()
n = counter(s)
print(n)
