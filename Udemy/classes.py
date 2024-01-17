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


# Create objects of class Account
customer1 = Account(cust_id="101", name="ABC")
customer2 = Account(cust_id="102", name="PQR")
customer3 = Account(cust_id="103", name="XYZ")
customer4 = Account(cust_id="104", name="LMN")

# Perform transactions
print(f"Customer 1 details: {customer1.get_details()}")
print(f"Current balance of Customer 1: {customer1.get_balance()}")
deposit_amount = 50000
print(
    f"After depositing {deposit_amount}, Customer 1 balance has balance: {customer1.deposite(amount=deposit_amount)}"
)
withdraw_amount = 5000
print(
    f"after withdrawing {withdraw_amount}, Customer 1 balance has balance: {customer1.withdraw(withdraw_amount)}"
)

# iteration over objects
customer2.deposite(5000)
customer3.deposite(10000)
customer4.deposite(50000)
print()

# Find customers without minimum balance of 10000 using iteration
customer_list = [customer1, customer2, customer3, customer4]
for customer in customer_list:
    if customer.balance < 10000:  # Min balance is set as 10000
        print(
            f"Customer with ID {customer.id} and name {customer.name} does not have minimum balance of 10000"
        )
