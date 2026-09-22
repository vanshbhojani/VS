class bankaccount:
    def __init__(self,balance):
        self.balance=balance

    def deposit(self,amount):
        self.amounr+=amount

    def get_balance(self):
        return self.balance

acc=bankaccount()
acc.deposit()

print("account balance is :",acc.get_balance())
