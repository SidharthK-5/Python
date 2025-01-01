"""
Question:
Find if the postal code is valid or not
Criteria:
1. Only six digit nos
2. There should not be more than 1 alternating repeatition of digits
"""

import re


"""
regex_integer_in_range: Checks for non zero start and exact 6 digit length code
"""
regex_integer_in_range = r"^[1-9]\d{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

"""
For alternating pattern: (\d) denotes the first group, which is only a digit
Positive lookahead assertion in 2nd group `(?=\d\1)` is used find match for first group.
\d between assertion ?= and \1 matches a single digit (b/w repeated characters)
\1 backreferences the digit captured in 1st group, ensuring it is same as the one in 1st group   
"""


P = input()

#   code is matched for validity and made bool        find all alternating repititive pair and the count is checked
print(
    bool(re.match(regex_integer_in_range, P))
    and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2
)
