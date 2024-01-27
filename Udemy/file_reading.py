"""
File reading methods
"""

# Read the file to memory
file = open("data/sample_file.txt", "r")

# read() will take number of char needed as argument. Else it will read the full file
# Read will return a string object
print(file.read(7))

# readlines() - Read all lines, but return type is list
content = file.readlines()
print(
    content[:1]
)  # Prints only first line. Since the earlier statement covered upto 7 characters, this statement will print rest of the characters in the line

# readline() - Reads line by line only
content = file.readline()
print(content)
# DO this iteratively
