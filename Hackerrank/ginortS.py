"""
Question:
Sort a string S using following coditions
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Eg: "Sorting1234" will be sorted to "ginortS1324"
"""

# Accept the input string from user
input_string = input()

ginortS = []
lowercase_letters = []
uppercase_letters = []
odd_numbers = []
even_numbers = []

# Check the ASCII value of each character and append it to it's corresponding list
for character in input_string:
    if ord(character) in range(97, 123):
        lowercase_letters.append(character)
    elif ord(character) in range(65, 91):
        uppercase_letters.append(character)
    elif ord(character) in range(48, 58):
        if ord(character) % 2 == 1:
            odd_numbers.append(character)
        else:
            even_numbers.append(character)

# Sort and combine the individual lists
ginortS = (
    sorted(lowercase_letters)
    + sorted(uppercase_letters)
    + sorted(odd_numbers)
    + sorted(even_numbers)
)
print("".join(ginortS))
