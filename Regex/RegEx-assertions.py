"""
Demo of RegEx assertions
"""
import re

"""
Positive lookahead check if there is a pattern ahead (to the right) or not
Negative lookahead is to assure that search string is not followed by lookahead regex, i.e., not present towards the right
"""

"""
+ve lookahead for a set of alnum (\w+) which is a first group
Lookahead is such that there is atleast one char gap (\w+) between 1st group and match
Here, captured group is 1st 'geeks'. There is another character group 'geeks' which occured after some characters
"""
print(re.search(r"(\w+)(?=\w+\1)", "geeksforgeeks").group())

"""
-ve lookahead is used to avoid repitition of same group with some character interval
Here, last 'geeks' is captured since there is no other group 'geeks' left in the string
"""
print(re.search(r"(geeks)(?!\w+\1)", "geeksforgeeks").group())
