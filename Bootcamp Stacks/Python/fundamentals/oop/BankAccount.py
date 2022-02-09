class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        balance += amount
    def withdraw(self, amount):
        if balance < 0:
            balance -= 5
            print('Insufficient funds: Charging a $5 fee')
             balance -= amount
    def display_account_info(self):
        print(f'Balance:$ {balance}')
    def yield_interest(self):
        if balance > 0:
            balance += (balance * int_rate)

Account_0101 = BankAccount(.21,200)
account_102 = BankAccount(.05,1000)