"""
Dictionary creation, updation and deletion
"""

print("Dictionary creation with two lists")

key_list = [1, 2, 3, 4, 5]
value_list = [1, 4, 9, 16, 25]
print(f"Lists are {key_list=}  {value_list=}")

dictionary = dict(zip(key_list, value_list))
print(dictionary)

print("\nDictionary from one list")
print("Using fromkeys()")

lst = [1, 2, 3, 4, 5]
dict1 = dict.fromkeys(lst, 0)
print(dict1)

print("\nMerging two dictionaries")

dict2 = {1: 1, 2: 4, 3: 9}
dict3 = {4: 16, 5: 25}
print(f"Dictionaries are {dict2=}  {dict3=}")
dict2.update(dict3)
print(dict2)

print("\npop()")
removed = dict2.pop(5)
print(dict2, removed)

print("\npopitem()")
removed = dict2.popitem()
print(dict2, removed)

print("\nclear()")
dict2.clear()
print(dict2)

print("\ndel method")
del dict2
