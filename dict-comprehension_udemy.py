# Square dict
d = {x: x**2 for x in range(1, 6)}
print(d)

# ASCII dict
d = {chr(i): i for i in range(97, 123)}
print(d)

# Swapping key and value
d1 = {value: key for key, value in d.items()}
print(d1)
