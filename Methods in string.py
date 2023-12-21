# Python strings

""" List Slicing """

s = "Python sample string"

# Slicing string_name[start : end - 1]
print(s[0:6])   # Prints Python = s[:6]
print(s[7:])

""" List Striding """

# Printing all alternate values
print(s[::2]) # Striding is like step in range() function
print(s[::-1])

for i in s[::2]:
    print(i)
