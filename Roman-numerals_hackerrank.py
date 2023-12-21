regex_pattern = r"^(C{,3})?(I{,3})?(M{,3})?(X{,3})?(L{,1})?(V{,1})?(D{,1})?$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))