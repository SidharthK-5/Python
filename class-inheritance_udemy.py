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
    
    def __init__(self, cust_id, name, initial_balance = 0):
        self.__id = cust_id
        self.__name = name
        self.__balance = initial_balance
        #Account.count += 1
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

class Savings_acc(Account):
    def __init__(self, cust_id, name, initial_balance=0):
        super().__init__(cust_id, name, initial_balance) # To pass id and name to parent class in order to avoid writing code again
        self.limit = 50000

    # Method overriding
    def withdraw(self, amount):
        if amount < self.limit:
            self.limit -= amount
            return super().withdraw(amount)
        else:
            print("Daily limit reached")

c1 = Savings_acc("101", "ABC")
# print(c1.__dict__)
print(c1.deposite(80000))
print(c1.withdraw(40000))
print(c1.withdraw(40000))

"""
Multiple inheritance
class A:
    pass
class B:
    pass
class C(A, B):
    pass
"""