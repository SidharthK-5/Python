"""
Question:
Given certain no. of usernames and mail IDs
Using email.utils, print the valid usernames and IDs
"""

import email.utils as eutils
import re

mail = "^[a-zA-Z][a-zA-Z0-9\.\-\_]+[@][a-z]+[\.][a-z]{1,3}$"
"""
username: Starts with an alphabet, rest of the characters can be alphanumeric, '.', '-' or '_'
domain: Only alphabelts
extension: Only alphabets, length can only be 1, 2 or 3
"""

n = int(input())
test_cases = []
for i in range(n):
    test_cases.append(input())

valid_emails = []
for case in test_cases:
    """
    parseaddr will separate input text into username and email address
    'DOSHI <DOSHI@hackerrank.com>' -> ('DOSHI', 'DOSHI@hackerrank.com')
    """
    username, mail_id = eutils.parseaddr(case)[0], eutils.parseaddr(case)[-1]
    if re.match(mail, mail_id):
        valid_emails.append(case)

for mail in valid_emails:
    print(mail)
