class Account:
    def __init__(self, cust_id, name, initial_balance=0):
        self.id = cust_id
        self.name = name
        self.balance = initial_balance

    def get_details(self):
        return " ".join([self.id, self.name])

    def get_balance(self):
        return self.balance

    def deposite(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return self.balance


customer1 = Account("101", "ABC")
customer2 = Account("102", "PQR")
customer3 = Account("103", "XYZ")
customer4 = Account("104", "LMN")
# print(customer1.id, customer1.name)
print(customer1.get_details())
print(customer1.get_balance())
print(customer1.deposite(50000))
print(customer1.withdraw(5000))

# iteration over objects
customer2.deposite(5000)
customer3.deposite(10000)
customer4.deposite(50000)

l = [customer1, customer2, customer3, customer4]
for obj in l:
    if obj.balance < 10000:  # Min balance is set as 10000
        print(obj.id, obj.name)
