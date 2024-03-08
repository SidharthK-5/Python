# Familiarization to RegEx module

import re

"""
. - any charater can be replaced with period symbol
[a-z] - lowercase char
[A-Z] - uppercase char
[a-zA-Z] - any letter
[a-Z] - any uppercase or lowercase character
[0-9] or \d - any digit
\D gives anything other than digits (complement)
[a-zA-Z0-9] or \w any alphanumeric
\W alphanumeric complement

\s - space
\S - space complement
+ - atleast one occurence. Eg: [a-z]+
* - zero or more occurences

^ - start of the string
$ - end of the string

[^a-n] means complement of a-n
^[a-n] means string starts with a-n


? - optional: The character or group just before ? is treated as optional

{} - range of items. Eg: [a-z]{2,4} means char a-z can appear 2 to 4 times

Assertions -> lookaheads -> positive lookaheads
?= - Assertion. used to check if the condition is true or not
eg:- ?=.* - assertion to match any character (.), zero or more times (*)
regex = '(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]{6,})' # atleast one lowercase, one uppercase, one num and should be 6 chara long

"""

# Checking PAN no. (5 uppercase, then 4 digits, then 1 uppercase)
string = "ABCDE1234A"
pattern = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")
# ^ to specify start ans $ to specify end else findall will grab strings which have 'r' as substrings
matches = re.findall(pattern, string)
print(f"{string=}  {pattern=}  {matches=}")

# Checking phone no
string = "7012310580"
pattern = re.compile("^[6-9][0-9]{9}$")
matches = re.findall(pattern, string)
print(f"{string=}  {pattern=}  {matches=}")

# Checking date format
string = "05/07/2022"
pattern = re.compile("^[0-9]{2}/[0-9]{2}/[0-9]{4}$")
matches = re.findall(pattern, string)
print(f"{string=}  {pattern=}  {matches=}")
