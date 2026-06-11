# mobile information 
# create a class called mobile 
#requirement :
#store mobile brand and price using object member .
#create 2 different objects
#diaplay both object details. separately.
#add a class member called categiry = "Electronics"


class Mobile :
    buttons = 3 
    camera = 3
    diaplay = 1 

    def __init__ (self , brand , ui , soft , Mah, price):   #constructor
        self.brand = brand
        self.ui = ui
        self.software = soft
        self.battery = Mah
        self.price = price

    def show(self):
        print("Brand Name :" , self.brand)
        print("UI" , self.ui)
        print("software" , self.software)
        print("battery" , self.battery)
        print("price" , self.price)

    
redmi = Mobile("Redmi" , "MIUI" , "Android" , 5000 , 13600)

print(redmi.show())
    