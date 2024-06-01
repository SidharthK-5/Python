"""
Greediness and Negative lookahead in RegEx
Greedy - .*
Non Greedy - .*?
? means optional
.* means any chara occurence 0 or more times.
But this is greedy, so it will look for as many chara in b/w - Greediness

Adding ? at the end will solve this
.*? looks for least no of occurences.
So this can limit occurences to 0 if possible - Non greediness
"""

import re



text = "abababcdefabgfujhg"
pattern = "ab.*?"
print(f"{pattern=}  {text=}")
print(re.findall(pattern, text))  # Gets all occurernces of "ab" in the text

text = "peter piper picked a peck of pickled peppers"
pattern = "p.*?e.*?r"
print(f"\n{pattern=}  {text=}")
print(re.findall(pattern, text))  # Gets all occurernces of "p...e...r" in the text

"""
Problem 1
find a match starting with 'crypto' and ending with 'coin' with atmost 30 chara in b/w
"""

text = "crypto-bot that is trading Bitcoin and other currencies"
pattern = "crypto(.{1,30})coin"
print(f"\n{pattern=}  {text=}")
print(re.match(pattern, text))

"""
Problem 2
Given a string. Find all dollar amounts with optional RegEx decimal values
"""

text = """If you invested $1 in the year 1801, you would have $18087791.41 today.
This is a 7.967% return on investment.
But if you invested only $0.25 in 1801, you would end up with $4521947.8525."""
pattern = "(\$[0-9]+(\.[0-9]+)?)"
"""
Breaking down the regex:
\$ - to escape the dollar sign
[0-9]+ - 1 or more digits
(\.[0-9]+)? - optional decimal part

the whole price value is taken as a group and the decimal part is taken as a sub group
# so even if there is no decimal part, price will be captured.
# o/p (whole price, decimal part)
"""
print(f"\n{pattern=}  {text=}")
print(re.findall(pattern, text))

"""
Problem 3
Replace Alice Wonderland with 'Alice Doe',
but not to replace occurences of 'Alice Wonderland' within single quotes
"""
# Negative lookahead ?!
# If -ve lookahead is given before a character,
# it will search for that character before the occurence of regex pattern

text = """
Alice Wonderland married to John Doe.
The new name of former 'Alice Wonderland' is Alice Doe.
Alice Wonderland replaces her old name 'Wonderland' with 'Doe'.
Alice's sister Jane Wonderland still keeps her old name.
"""
pattern = "Alice Wonderland(?!')"
"""
Regex breakdown:
-ve lookahead (?!) checks for the occurence of ' before Alice Wonderland.
If found, substitution function wont be applied.
"""
print(f"\n{pattern=}  {text=}")
print(
    re.sub("Alice Wonderland(?!')", "Alice Doe", text)
)
