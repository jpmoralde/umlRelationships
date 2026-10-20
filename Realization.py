from abc import ABC, abstractmethod

class Payable(ABC):
    @abstractmethod
    def pay(self):
        pass
class Payment(Payable):
    def pay(self):
        print("Payment made")
payment = Payment()
payment.pay()