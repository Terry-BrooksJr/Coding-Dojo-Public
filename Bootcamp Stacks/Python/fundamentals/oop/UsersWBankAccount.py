class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount): #Wanted to add added complexity. This account will only charage the 5 dollar fee if the withdrawl amount is greater than 5 dollars. 
        if amount > 5 and amount > self.balance:
            self.balance -= 5
            print('Insufficient funds: Charging a $5 fee')
        if amount < 5 and amount > self.balance: 
            self.balance -= amount
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f'Balance:$ {self.balance}')
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
class User:
    def __init__(self, first_name, last_name, age, opening_deposit):
        self.first_name  = first_name
        self.last_name = last_name
        self.age = age
        self.account_balance = BankAccount(int_rate=0.02,balance = opening_deposit)
    def make_withdrawal(self, amount):
        self.BankAccount.withdraw(self, amount)
    def display_user_balance(self):
        self.BankAccount.display_account_info(self)
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
    def make_deposit(self, amount):
        self.BankAccount.deposit(self, amount)
