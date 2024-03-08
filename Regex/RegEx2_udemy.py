import re

print("Groups in RegEx")
string = "05/07/2022"
#  () refers to one group
pattern = re.compile("^([0-9]{2})/([0-9]{2})/([0-9]{4})$")
print(f"{string=}  {pattern=}")

# Search method in re
match = re.search(pattern, string)
if match:
    # group(0) all grps combined, group(1 or 2 or 3) gives particulat indexed grp
    print(f"{match.group()=}")
    print(f"{match=}")
else:
    print("Pattern not found")

print("\nNamed groups")
string = "05/07/2022"
pattern = re.compile("^(?P<date>[0-9]{2})/(?P<month>[0-9]{2})/(?P<year>[0-9]{4})$")
print(f"{string=}  {pattern=}")

match = re.search(pattern, string)
if match:
    print(f"{match.group('date')=}")
    print(f"{match.group()=}")
else:
    print("Pattern not found")

print("\nOptional non-capturing groups")
string = "+91 7012310580"

# \+ is for escaping + as operator. ? will consider its prior grp as optional
pattern = re.compile("(\+91\s)?([6-9][0-9]{9})")

# ?: denotes non-capturing grp. So index 1 will only show actual phone no
pattern = re.compile("(?:\+91\s)?([6-9][0-9]{9})")

print(f"{string=}  {pattern=}")

match = re.search(pattern, string)
if match:
    print(f"{match.group(1)=}")
else:
    print("Pattern not found")
