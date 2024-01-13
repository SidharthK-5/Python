"""
Reading a file using python
"""

# If we open a file, it should be closed with file.close() method after use
my_file = open("data/sample_file.txt", "r")
print(my_file.read())
my_file.close()
print("\n\n")

# To avoid close(), we can use "with" statement
# with is called context manager since it avoids creating a file variable and need for closing
with open("data/sample_file.txt", "r") as temp_file:
    rf = temp_file.read()
print(rf)
