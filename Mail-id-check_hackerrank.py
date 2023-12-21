#import email.utils
import re
mail = "^[<][a-zA-Z][a-zA-Z0-9\.-_]+[@][a-z]+[a-z]{1,3}[>]$"

n = int(input())
d = {}
for i in range(n):
    key, val = map(str, input().split())
    d[key] = val

for k, v in d.items():
    # if email.utils.formataddr((k, v)):
    #     print(k, v)
    if re.match(mail,v):
        print(k,v)

