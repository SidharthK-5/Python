"""
Operations on files
"""

# In w+ mode, we can write as well as read. But file pointer reached the end.
f = open(
    "data/input2.txt", "w+"
)  # write creates new file if it doesnt exist. if exists, it overwrites the contents

f.write("line 1")

"""
tell() and seek()
tell() - gives the current file pointer position
seek(offset, pos) - moves file pointer from 'pos' with 'offset' no of characters
                  offset - no of chara
                  pos - 0 for start of file, 1 for current pos, 2 for end of file
      for pos 1 and 2, offset should be 0, else it will give error
"""
      
print(f.tell())
f.seek(0, 0)  # Moves file pointer 0 chara from start
print(f.tell())
content = f.read()
print(f.tell())
print(content)
f.close()

"""
w+ and r+
w+ re-writes and allows to read
r+ will read without re-writing, but allows to add more content
"""

f = open("data/input2.txt", "r+")
print(f.read())
f.write("\n\nNewline added")
print(f.read())
f.close()

"""
a and a+
The file pointer will be at the end by default, whereas in r and w, file pointer is at the start
"""

f = open("data/input2.txt", "a+")  # a+ can append and read
f.write("\n\nLast line")
