"""
Find valid time from the given list
time format hh:mm
"""

import re

inputs = ["18:29", "23:55", "123", "ab:de", "18:299", "99:99"]
print(f"{inputs=}")

print("\nMatch only numerical values")
print([re.fullmatch("[0-9]{2}:[0-9]{2}", value) for value in inputs])

print("\nValidate time only between 00:00 to 23:59")
regex_pattern = "([01][0-9]|2[0-3]):([0-5][0-9])"
print([re.fullmatch(regex_pattern, value) for value in inputs])
