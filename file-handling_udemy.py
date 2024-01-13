f = open("sample_file.txt", "r")
# read() will take no of char needed as argument. Else it will read the full file
# Read will return a string object
print(f.read(7))

# readlines() - Read all lines, but return type is list
content = f.readlines()
print(
    content[:1]
)  # Prints only first line. Since the earlier statement covered upto 7 characters, this statement will print rest of the characters in the line

# readline() - Reads line by line only
content = f.readline()
print(content)
# DO this iteratively
