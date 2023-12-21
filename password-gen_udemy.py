import random

# Default argument
def gen_password(length = 8): # Setting default value of legth as 8
    l = ['@','#','$','&']
    upper = chr(random.randint(65,90))
    lower = chr(random.randint(97,122))
    special = random.choice(l)
    digit = random.randint(10000,99999)
    password = upper + lower + special + str(digit)
    l = random.sample(password,length)
    password = ''.join(l)
    return password

result = gen_password()
print(result)

# Keyword Argument
def validate(username, password):
    if username == "ABC" and password == "Abc@123":
        print("Valid password")
    else:
        print("Invalid password")

validate("ABC", "Abc@123")
validate("Abc@123", "ABC")
validate(password="Abc@123", username="ABC")