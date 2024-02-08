"""
Generate password using random library and password validation
"""

import random


# Default argument
def generated_password(length=8):  # Setting default value of legth as 8
    special_characters = ["@", "#", "$", "&"]
    upper = chr(random.randint(65, 90))
    lower = chr(random.randint(97, 122))
    special = random.choice(special_characters)
    digit = random.randint(10000, 99999)
    password = upper + lower + special + str(digit)
    scrambled = random.sample(password, length)
    password = "".join(scrambled)
    return password


password = generated_password()
print(f"Generated password = {password}")

def validate_user(username, password):
    if username == "ABC" and password == "Abc@123":
        print("Valid password")
    else:
        print("Invalid password")


validate_user("ABC", "Abc@123")
validate_user("Abc@123", "ABC")

# Keyword Argument
validate_user(password="Abc@123", username="ABC")
