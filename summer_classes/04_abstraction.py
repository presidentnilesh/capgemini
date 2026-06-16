from abc import ABC , abstractmethod

class BankApp(ABC) :
    @abstractmethod
    def Account_no():
        pass
class MobileApp(BankApp):
    def Account_no(self):
        print("i am safe")

def Account_No(BankApp):
    pass
m= MobileApp()
m.Account_no()



