class bank:
    def __init__(self):
        self.balance = 0
    def create_account(self, account):
        self.account = account
        if len(account)!= 26:
            print('ERROR!!')
    def withdraw(self, amount):
        if int(amount)>self.balance:
            print('Insufficient funds on the account')
        else:
            self.balance -= int(amount)
            print(f'{amount}$ has been withdrawn')
    def deposit(self, cash):
        self.balance += int(cash)
        print(f'You have deposited {cash}$')
    def show_status(self):
        print(f'Bank account no: {self.account}')
        print(f'Balance: {self.balance}$')