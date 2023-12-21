# If we open a file, it should be closed with file.close() method after use
my_file = open("sample_file.txt", "r")
print(my_file.read())
print("\n\n")
# To avoid close(), we can use with statement - with is called context manager since it avoids creating a file variable and need for closing
with open("sample_file.txt", 'r') as temp_file:
    rf = temp_file.read()
print(rf)