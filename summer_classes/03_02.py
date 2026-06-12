# when there is no init(initialiazation) in the child class then the init of parent class will print or will perform ... but when there is init in the child class then the init of the child will pe/

# class Pen :
#     def __init__(self , price , color):
#         self.price = price 
#         self.color = color 
#         print("in parent class ")

#     def Write(self):
#         print("writing")

# class Student(Pen):
    # pass
#     def __init__ (self , name , age):
#         print("in child class")
#         self.name = name 
#         self.age = age
#     def show(self):
#         print("name" , self.name , "\n age:" , self.age)

# st = Student(99 , 90)


class Phone():
    def __init__(self ):
        print("inside phone constructor")
        self.__price = 1000 
        self.brand = "ABC"

        #getter
        def show(self):
            print(self.__price)
        
class SmartPhone(Phone):
    def __init__(self , ram, os):
        self.os = os 
        self.ram = ram 
        print("Inside child constructor ")

s=SmartPhone("8" , "Android")
print(s.os())
print(s.ram())