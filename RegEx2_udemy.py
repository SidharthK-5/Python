import re

# Groups in RegEx

s = "05/07/2022"
r = re.compile("^([0-9]{2})/([0-9]{2})/([0-9]{4})$") # putting in () makes the data in groups

# Search method in re
m = re.search(r,s)
if m:
    print(m.group()) # group(0) all grps combined, group(1 or 2 or 3) gives particulat indexed grp
    print(m)
else:
    print("Pattern not found")

# Named groups
s = "05/07/2022"
r = re.compile("^(?P<date>[0-9]{2})/(?P<month>[0-9]{2})/(?P<year>[0-9]{4})$")

m = re.search(r,s)
if m:
    print(m.group("date"))  
    print(m.group())
else:
    print("Pattern not found")

# Optional non-capturing groups
s = "+91 7012310580"
r = re.compile("(\+91\s)?([6-9][0-9]{9})") # \+ is for escaping + as operator. ? will consider its prior grp as optional
r = re.compile("(?:\+91\s)?([6-9][0-9]{9})") # ?: denotes non-capturing grp. So index 1 will only show actual phone no
m = re.search(r,s)

if m:
    print(m.group(1))
else:
    print("Pattern not found")