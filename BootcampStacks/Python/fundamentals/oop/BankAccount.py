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

account_0101 = BankAccount(.21,200)
account_0102 = BankAccount(.05,1000)

account_0101.deposit(200).deposit(500).deposit(2).withdraw(5000)
account_0102.deposit(150).deposit(50).withdraw(200).withdraw(5).withdraw(200).withdraw(1).yield_interest().display_account_info()
