import re

if __name__ == "__main__":
    s = input()
    # print(any(i.isalnum() for i in s))
    # print(any(i.isalpha() for i in s))
    # print(any(i.isdigit() for i in s))
    # print(any(i.islower() for i in s))
    # print(any(i.isupper() for i in s))

    print(bool(re.search("\w", s)))
    print(bool(re.search("[a-zA-Z]", s)))
    print(bool(re.search("\d", s)))
    print(bool(re.search("[a-z]", s)))
    print(bool(re.search("[A-Z]", s)))
