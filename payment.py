from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class Creditcard(Payment):
    def pay(self,amount):
        print(f"paid {amount} using Credit Card")
class UPI(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using UPI")
payment1= Creditcard()
payment1.pay(600)
payment2=UPI()
payment2.pay(5000)
