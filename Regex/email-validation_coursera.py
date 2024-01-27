"""
Email Validation. An e-mail is valid is it satisfies the following conditions
1. username : alphanumeric or . or _ or -
2. domain name : alphanumeric
3. extension : alphanumeric, 2 or 3 chara long
"""

import re

inputs = ["ro$g45@gmail.com", "r_duke78o@outlook.coma", "s.rog78o@outlook.com"]
regex = "^(\w|\.|\-|\_)+[@]\w+[\.]\w{2,3}$"
"""
Regex pattern breakdown:
1. ^ and $ -> specifies strict start and end of the string
2. (\w|\.|\-|\_)+ -> First group can have either alphanumeric, '.', '-' or '_', '+' for one or more occurences
3. [@] -> Matches one occurence of '@'
4. \w+ -> Alphanumeric, one or more occurences
5. [\.] -> Matches one occurence of '.'
6. \w{2,3} -> Alphanumeric, 2 to 3 occurences
"""

print([re.fullmatch(regex, x) for x in inputs])
