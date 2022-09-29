# User Class

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(balance = 5000, int_rate = 0.02)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)
        return self

    def display_user_balance(self):
        print(self.account.balance)
        return self


# Bank Account Class

class BankAccount:

    def __init__(self, balance, int_rate):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance = (self.balance + amount)
        return self
    
    def withdraw(self, amount):
        self.balance = (self.balance - amount)
        return self

user = User('Steve Tobias', 'sblaket@gmail.com')
user.make_deposit(4500).make_withdrawal(2000).display_user_balance()



