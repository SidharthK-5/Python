"""
Question:
Find valid E-mail addresses from the input values and print them in a list. Valid E-mails are:
    1. Username can be alnum, - or _
    2. domain name can be alnum only
    3. extension can be max 3 alphabets
"""

import re


def validate_mail_id(email_id: str) -> bool:
    """
    return True if 'email' is valid, else False

    Args:
        email (str): email ID to be checked

    Returns:
        bool: tells if the email ID is valid or not
    """
    email_pattern = re.compile("^(\w|\-|\_)+[@][a-zA-Z0-9]+[\.][a-zA-Z]{,3}$")
    if re.match(email_pattern, email_id):
        return True
    else:
        return False


def filter_mail(emails: list[str]) -> list[str]:
    """
    finds the valid email IDs from the given list of strings

    Args:
        emails (list[str]): all strings to be checked

    Returns:
        list[str]: valid email IDs from input
    """
    # filter is a function to select values from an iterator, based on true or false condition of a function
    return list(filter(validate_mail_id, emails))


if __name__ == "__main__":
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
