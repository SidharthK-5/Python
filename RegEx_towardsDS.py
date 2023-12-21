import re
text = 'I have called the service desk 100 times and nobody replies to me. I need a conversation ASAP!! My number is 111-1234567! My other number is 7654321!'
result = re.findall('111-1234567', text) # When we fully know what to look
print(result)
result = re.findall("\d",text) # select all digits
print(result)
result = re.findall("\d+",text) # select all numbers, not digits
print(result)
result = re.findall("\d{3}-\d{7}",text) # select strings of this type
print(result)

# Optional area code
result = re.search("(\d{3}-)?(\d{7})",text)
print(result.group())

result = re.findall("\d{3}-\d{7}|\d{7}", text)
print(result)

# Repitition
text = "abcabc aa cc dd e 123123 abcabab"
result = re.findall(r"(\w{3})(\1)", text)
print(result)
result = re.findall(r"(\w{3})(\w{2})(\2)", text)
print(result)