# multi-level inheritance 

# class Car():
#     color = "Black"
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("the cas has been stoped")

# class ToyotaCar(Car):
#     def __init__(self , brand):
#         self.brand= brand 

# class Foortuner(ToyotaCar):
#     def _init__(self , type):
#         self.type = type
        

# car1=Foortuner("SUV")
# car2=ToyotaCar("Top")

# car2.stop()
# car1.stop()




    # multiple inheritance 

# class A :
#     varA = ("welcome to class A")

# class B :
#     varB = ("welcome to class B")

# class C(A , B):
#     varC = ("welcome to class C")

# c1=C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)


    #Method 

class Car():
    def __init__(self , type):
        self.type = type

    
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("the cas has been stoped")

class ToyotaCar(Car):
    def __init__(self , brand):
        self.brand= brand 

class Foortuner(Car):
    def __init__(self , name , type):
        self.name = name
        super().__init__(type)  # as there is init in the child class but child want to inherit from the parent class . therefore we can use the syper() so that i ca also inherit from its parent dispite having init. in child class . 
        super().start()     # we called the start method 

c1 = Foortuner("sexy", "petrol")
print(c1.type)
        