# Dictionaries

d = {"emp_id": 101, "name": "ABC", "email": "abc@gmail.com"}
d["contact_no"] = 1234567890
print(d)
d["contact_no"] = 8523697
print(d)

""" get() is used to access value at a key. It returns 'None' if key is not
present. dict_name[key] will throw error if key is not found """

print("get() method :", d.get("age"))  # return 'None' can be changed as a 2nd arguement

print("\nsetdefault() to specify default value to a key which is not defined")
d.setdefault("age", 25)
print(d)

print("\nChecking if 'age' is a key in 'd'")
print("age" in d)

print("\nIterating throgh a dictionary")
for key in d:
    print(key, d[key])

d1 = {}
for value in range(1, 11):
    d1[value] = value**2
print(d1)

print("\nkeys() :", d.keys())
print("values() :", d.values())
print("items() :", d.items())  # Prints a tuple of items
# Another method to print items as tuple
for t in d.items():
    print(t, end="\t")
