import re

# To find if the same character repeats next to it. \1+ after the group checks for repition of 1st group
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
if m:
    print(m.group(1))
else:
    print(-1)
