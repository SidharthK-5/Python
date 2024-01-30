"""
Slicing and Striding in string
"""

# List Slicing

sample_string = "Python sample string"
print(f"{sample_string=}")

# Slicing string_name[start : end - 1]
print("\nSlicing Examples...")
print(f"Print only first 7 characters: {sample_string[0:6]}")
print(f"Print from 8th character onwards: {sample_string[7:]}")

"""
List Striding
Striding is like step in range() function
"""

print("\nStriding Examples...")
print(f"Print only alternating characters: {sample_string[::2]}")
print(f"Print the reverse of sample string: {sample_string[::-1]}")

print("\nPrint alternating characters with a loop")
for character in sample_string[::2]:
    print(character, end=" ")
