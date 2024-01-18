"""
Question:
Split the given string at the occurences of ',' or '.'
Print the substrings line by line
"""

import re

# re.split() splits the string when the given re pattern is found
regex_pattern = r"[,.]"  # Pattern to detect

# when regex_pattern is found in the input, split breaks it at the pattern
print("\n".join(re.split(regex_pattern, input())))
