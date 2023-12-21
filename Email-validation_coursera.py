# Email validation
# username : alnum or . or _ or -
# domain name : alnum
# extension : alnum, 2 or 3 chara long

import re

inputs = ['ro$g45@gmail.com', 'r_duke78o@outlook.coma', 's.rog78o@outlook.com']
regex = '^(\w|\.|\-|\_)+[@]\w+[\.]\w{2,3}$'

print([re.fullmatch(regex, x) for x in inputs])