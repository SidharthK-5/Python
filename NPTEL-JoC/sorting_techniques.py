lst = ["aaaa", "bbb", "cc", "d"]

print(sorted(lst))  # Sort list alphabetically
print(sorted(lst, key=len))  # Sort list by length of elements
print(sorted(lst, key=lambda x: x[-1]))  # Sort list by last character of each element
print(
    sorted(lst, key=lambda x: x[-1], reverse=True)
)  # Sort list by last character in reverse order
print(sorted(lst, key=lambda x: x[0]))  # Sort list by first character of each element
print(
    sorted(lst, key=lambda x: x[0], reverse=True)
)  # Sort list by first character in reverse order
