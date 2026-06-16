# hi i am here for the capgemini classes and i am not feeling good as becaus ei am not too good at cooding and i believe that i can be the one that can do 

# Abstraction 
  
#super()

# class Phone:
#     def buy(self):
#         print("parent ")

# class SmartPhone(Phone):
#     def buy(self):
#         super().buy()
#         print("child")

# s1=SmartPhone()
# s1.buy()

# question 2 

# class Phone :
#     def __init__(self , price , brand , camera):
#         self.price = price 
#         self.brand = brand 
#         self.camera = camera 

#     def buy(self):
#         print("Buying phone ")

# class SmartPhone(Phone):
#     def buy(self):
#         print("Buying phone ")
#         super().buy()
#         # print(super().brand)    # super can only access method but not member 

# s = SmartPhone(2000 , "apple" , 13)

# s.buy()


# calling constructor by using super 

class Phone :
    def __init__(self , price , brand , camera):
        self.price = price 
        self.brand = brand 
        self.camera = camera

    def show(self):         
        print("price of the smartphone is :" , self.price )
        print("brand of the smartphone is :" , self.brand )
        print("camera of the smartphone is :" , self.camera )
        
class SmartPhone(Phone):
    def __init__(self , brand  , price , camera , os , ram  ):
        print("Inside Smartphone construction ")
        self.os = os 
        self.ram = ram 
        super().__init__(price , brand , camera)

    def show(self):
        print("price of the smartphone is :" , self.price )
        print("brand of the smartphone is :" , self.brand )
        print("camera of the smartphone is :" , self.camera )
        print("os of the smartphone is :" , self.os )
        print("ram of the smartphone is :" , self.ram )
        
        
s1 = SmartPhone("samsung" , 34433 , 50 , "android" , 6)
s1.show()
        