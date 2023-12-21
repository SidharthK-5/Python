""" Question: Find consecutive vowel repitions if they are bound by consonants """

import re

consonants = "[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]"
vowels = "^[aeiouAEIOU]{2,}"
S = input()
l = []

i = 0
while i < len(S):
    if re.match(consonants, S[i]): # If starting letter of current string is consonant, then proceed
        m = re.match(vowels, S[i+1:len(S)-1]) # Checking consecutive vowel repitions in the string from next index to end-1 pos
        if m and re.match(consonants, S[i+len(m.group())+1]): # Checking if pattern is found and if the right side of pattern has consonant
            l.append(m.group()) # If so, add the pattern to list
        if m:
            i = i + len(m.group()) + 1 # Skipping the iteration over the length of current pattern by incrementing i with pattern length
        else:
            i += 1 # If pattern is not obtained even after getting a consonant start
    else:
        i += 1 # No consonant start

if len(l) > 0:
    print('\n'.join(l))
else:
    print(-1)
