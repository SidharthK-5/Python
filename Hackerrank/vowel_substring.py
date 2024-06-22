"""
Find consecutive vowel repitions if they are bound by consonants
"""

import re

consonants = "[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]"
vowels = "^[aeiouAEIOU]{2,}"
string = input()
vowel_groups = []

char_pos = 0
while char_pos < len(string):
    # If starting letter of current string is consonant, then proceed
    if re.match(consonants, string[char_pos]):
        # Checking consecutive vowel repitions in the string from next idx to end-1 pos
        match_found = re.match(vowels, string[char_pos + 1 : len(string) - 1])

        # Checking if pattern is found and if the right side of pattern has consonant
        if match_found and re.match(
            consonants, string[char_pos + len(match_found.group()) + 1]
        ):
            # If found, add the pattern to list
            vowel_groups.append(match_found.group())

        if match_found:
            """
            Skipping the iteration over the length of identified pattern
            Incrementing char_pos with pattern length
            """
            char_pos = char_pos + len(match_found.group()) + 1
        else:
            # If pattern is not obtained even after getting a consonant start
            char_pos += 1
    else:
        char_pos += 1  # No consonant start

if len(vowel_groups) > 0:
    print("\n".join(vowel_groups))
else:
    print(-1)
