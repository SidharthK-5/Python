class Account:
    # Class variable creation
    count = 0

    # Class method
    @classmethod
    def incr_count(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    # Static method - Here, cls variable and instance variables are not accessed
    @staticmethod
    def Print_val():
        print("Static method call")

    def __init__(self, cust_id, name, initial_balance=0):
        self.__id = cust_id
        self.__name = name
        self.__balance = initial_balance
        # Account.count += 1
        Account.incr_count()

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def deposite(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance"
        else:
            self.__balance -= amount
            return self.__balance


customer1 = Account("101", "ABC")

# Some techs in private members
# print(customer1.__dict__)
# print(customer1._Account__id)

customer2 = Account("102", "PQR")
customer3 = Account("103", "XYZ")
customer4 = Account("104", "LMN")
print(customer1.get_balance())
print(customer1.deposite(50000))
print(customer1.withdraw(5000))

# iteration over objects
customer2.deposite(5000)
customer3.deposite(10000)
customer4.deposite(50000)

# l = [customer1, customer2, customer3, customer4]
# for obj in l:
#     if obj.get_balance() < 10000: # Min balance is set as 10000
#         print(obj.get_id(), obj.get_name())

# print(Account.count)
# print(customer1.count)
# """
# Account.count = val - updates the value of count in all objects
# customer1.count = val - updates the value of count in customer1 only. This creates a new variable in customer1 and the change is not global
# """
# print(customer1.__dict__)
# customer1.count = 100
# print(customer1.__dict__)

print(Account.get_count())
print(Account.Print_val())
