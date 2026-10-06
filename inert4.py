class BankAccount:
    def __init__(self):
        self.account_type="Genric Account"
    def status(self):
        print("Account is active and accesible")
class Savings_Account(BankAccount):
    pass
savings=Savings_Account()
print("Accesed Parent Proptery:",Savings_Account)
savings.status()