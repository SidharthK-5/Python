""" Question : Find valid E-mail addresses from the input values and print them in a list. Valid E-mails are:
                1. Username can be alnum, - or _
                2. domain name can be alnum only
                3. extension can be max 3 alphabets"""

import re


def fun(s):
    # return True if s is a valid email, else return False
    email = re.compile("^(\w|\-)+[@][a-zA-Z0-9]+[\.][a-zA-Z]{,3}$")
    if re.match(email, s):
        return True
    else:
        return False


def filter_mail(emails):
    # filter is a function to select values from an iterator, based on true or false condition of a function. Function can be lambda
    return list(filter(fun, emails))


if __name__ == "__main__":
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
