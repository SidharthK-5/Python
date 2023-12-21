""" Question: Find number patterns with only 16 digit length, in groups of 4, contains only '-' as seperator,
                should not have numbers repeating more than 3 """

import re

# card is the pattern with 4,5 or 6 as start, optional seperator '-'
card = re.compile("^([4,5,6][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$")

result = []
N = int(input())
while N > 0:
    num = input()
    # Check match of card and num && search consecutive repitition of same no more than 3, with optional '-' seperator
    if re.match(card, num) and not(re.search(r'([0-9])(-?\1){3}', num)): # -? is put in paranthesis with \1 means - can be optional inside 1st group
        result.append("Valid")
    else:
        result.append("Invalid")
    N -= 1

print('\n'.join(result))