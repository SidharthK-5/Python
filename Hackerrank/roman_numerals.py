"""
Given a string, determine if it's a valid Roman numeral.
"""

import re


"""
Pattern is made up of 4 groups, each group representing a digit of the Roman numeral.
1. (M{0,3}): 1000's place. 0 to 3 Ms (1000).
2. (CM|CD|D?C{0,3}): 100's place. CM (900), CD (400), 0 to 1 Ds (500), 0 to 3 Cs (100).
3. (XC|XL|L?X{0,3}): 10's place. XC (90), XL (40), 0 to 1 Ls (50), 0 to 3 Xs (10).
4. (IX|IV|V?I{0,3}): 1's place. IX (9), IV (4), 0 to 1 Vs (5), 0 to 3 Is (1).

"""
regex_pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
print(str(bool(re.match(regex_pattern, input()))))
