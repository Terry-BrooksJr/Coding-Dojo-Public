import random

class User:
    def __init__(self, first_name, last_name, age, opening_deposit):
        self.first_name  = first_name
        self.last_name = last_name
        self.age = age
        self.account_balance = opening_deposit
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f'Account Holder: {self.last_name},{self.first}, Current Available Balance: $ {self.account_balance} USD.')
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

Lucky = User('Lucky','TA',32,2000)
Ryan = User('Ryan','Magley',32,10000)
Terry = User('Terry','Brooks',33,200)

Terry.make_deposit(600).make_deposit(5000).make_deposit(300).make_withdrawal(45.32)
print(Terry.account_balance)
Ryan.make_deposit(33.23).make_deposit(150).make_withdrawal(250.56).make_withdrawal(20.75).make_withdrawal(20.75).transfer_money(Lucky,150)
print(Ryan.account_balance)
Lucky.make_deposit(32).make_withdrawal(300)
Lucky.make_withdrawal(300).make_withdrawal(150).make_withdrawal(100)
print(Lucky.account_balance)
