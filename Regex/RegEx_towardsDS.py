import re

text = "I have called the service desk 100 times and nobody replies to me. I need a conversation ASAP!! My number is 111-1234567! My other number is 7654321!"
print(f"{text=}")
result = re.findall("111-1234567", text)  # When we fully know what to look
print(f"Pattern: '111-1234567'   Method: findall()   {result=}")

# find all digits, one digit at a time
result = re.findall("\d", text)
print(f"Pattern: '\d'   Method: findall()   {result=}")

# select all numbers, (digit groups)
result = re.findall("\d+", text)
print(f"Pattern: '\d+'   Method: findall()   {result=}")

# select strings of containing 3 digits, '-' and then 7 digits
result = re.findall("\d{3}-\d{7}", text)
print(f"Pattern: '\d{3}-\d{7}'   Method: findall()   {result=}")

# Optional area code
result = re.search("(\d{3}-)?(\d{7})", text)
print(f"Pattern: '(\d{3}-)?(\d{7})'   Method: search()   {result.group()=}")

result = re.findall("\d{3}-\d{7}|\d{7}", text)
print(f"Pattern: '\d{3}-\d{7}|\d{7}'   Method: findall()   {result=}")

# Repitition
text = "abcabc aa cc dd e 123123 abcabab"
print(f"\n{text=}")
result = re.findall(
    r"(\w{3})(\1)", text
)  # Three alnum, with 1st group repeating after itselft
print(f"Pattern: '(\w{3})(\\1)'   Method: findall()   {result=}")

result = re.findall(
    r"(\w{3})(\w{2})(\2)", text
)  # Three alnum, two alnum, with 2nd group repeating
print(f"Pattern: '(\w{3})(\w{2})(\\2)'   Method: findall()   {result=}")
