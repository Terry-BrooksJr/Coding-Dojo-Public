import random

class User:
    def __init__(self, first_name, last_name, age, opening_deposit):
        self.first_name  = first_name
        self.last_name = last_name
        self.age = age
        self.account_balance = opening_deposit
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self.account_balance
    def display_user_balance(self):
        print(f'Account Holder: {self.last_name},{self.first}, Current Available Balance: $ {self.account_balance} USD.')
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
    def make_deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

Lucky = User('Lucky','TA',32,2000)
Ryan = User('Ryan','Magley',32,10000)
Terry = User('Terry','Brooks',33,200)

Terry.make_deposit(600)
Terry.make_deposit(5000)
Terry.make_deposit(300)
Terry.make_withdrawal(45.32)
print(Terry.account_balance)
Ryan.make_deposit(33.23)
Ryan.make_deposit(150)
Ryan.make_withdrawal(250.56)
Ryan.make_withdrawal(20.75)
print(Ryan.account_balance)
Lucky.make_deposit(32)
Lucky.make_withdrawal(300)
Lucky.make_withdrawal(150)
Lucky.make_withdrawal(100)
print(Lucky.account_balance)

Ryan.transfer_money(Lucky,150)
