"""
Question:
Find valid credit card numbers that follow the below criteria
    1. Must start with 4, 5 or 6
    2. only 16 digit length
    3. Should only contain digits
    4. in groups of 4
    5. contains only '-' as seperator between groups or there should not be any separator
    6. should not have 4 or more consecutive repeating characters

"""

import re

# card is the pattern with 4,5 or 6 as start, optional seperator '-'
card_pattern = re.compile("^([4,5,6][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$")

result = []
num_cases = int(input())
while num_cases > 0:
    test_case = input()
    # Check match of card and num && search consecutive repitition of same no more than 3, with optional '-' seperator
    if re.match(card_pattern, test_case) and not (
        re.search(r"([0-9])(-?\1){3}", test_case)
    ):  # -? is put in paranthesis with \1 means - can be optional inside 1st group (for num repitition check)
        result.append("Valid")
    else:
        result.append("Invalid")
    num_cases -= 1

print("\n".join(result))
