class phone :
 
    def __init__(self , price , brand , camera ):
        print("inside phone constructor ")
        self.price = price
        self.brand = brand 
        self.camera = camera

    def buy(self):
      print("Buying Phone")

class SmartPhone(phone):
    pass



s1 = SmartPhone("300000", "Apple" , "32")
s1.buy()
print(s1())