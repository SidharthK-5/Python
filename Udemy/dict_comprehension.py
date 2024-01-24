"""
Methods to create dictionaries using comprehension
"""

# Square dict
print("Dictionary with key as number and value as their squares")
d = {x: x**2 for x in range(1, 6)}
print(d)

# ASCII dict
print("\nDictionary with key as alphabet and it's ASCII as value")
d = {chr(i): i for i in range(97, 123)}
print(d)

# Swapping key and value
print("\nSwapping key and value of the above dict")
d1 = {value: key for key, value in d.items()}
print(d1)
