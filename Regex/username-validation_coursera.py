"""
Username validation
username can contain only alphabets, _ and .
"""

import re

inputs = ["a_roger", "aroger", "a.roger_de", "a.roger_2"]
regex = "^[a-zA-Z_.]+$"

print([re.fullmatch(regex, x) for x in inputs])
