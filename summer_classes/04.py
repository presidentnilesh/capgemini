# constructor example

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

s1=SmartPhone("30,000", 'Samsung', '13px')
print(s1.price)
print(s1.brand)
s1.buy()