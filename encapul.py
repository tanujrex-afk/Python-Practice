class BankAccount:
    def __init__(self,init_bal=0):
        self.balance=init_bal
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited:${amount}")
        else:
            print("Deposit amount must be positive")
    def withdraw(self,amount):
        if amount<=0:
            print("withdrawal amount must be positive")
        elif amount<=self.balance:
            self.balance-=amount
            print("Transaction denied")
    def get_balance(self):
        return self.balance
# Access control
account=BankAccount(500000)
print(f"Initial Balance:${account.get_balance()}")
account.deposit(20000)
print(f"Balance after deposit:${account.get_balance()}")
account.withdraw(30000)
print(f"Balance after denied transaction:${account.get_balance()}")
try:
   print(account.balance)
except AttributeError:
    print("Access Blocked:u caanot read _balance directly from the outside the class")
try:
    account.balance=600000
    print(f"attempted bypass failed.Real balance is still:${account.get_balance()}")
except Exception:
    pass
 