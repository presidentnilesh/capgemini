


# # class Student :
# #     college_name = "cgc"
# #     course = "cse"
# #     location = "india"
# #     def __init__ (self , name , age , gender):    // init means initialization
# #         self.name = name
# #         self.age = age
# #         self.gender = gender 
# #         print("haanji")
    
# #     def show(self):
# #         print("name" , self.name)   # object instance variables
# #         print("age" , self.age)
# #         print("gender" , self.gender)

# # ob = Student('Uttam' , 23 , 'male')

# # print(ob.age)
# # print(ob.college_name)
# # print(ob.course)
# # print(ob.location)
# # print(ob.gender)
# # print(ob.name)


    
    
# # anand = Student("Anand" , 21 , "male")
# # sandeep = Student("sandeep" , 20 , "female")

# # (anand.show())
# # (sandeep.show())




# #         # object method 

# # class dog :
# #     species ="canibal"
# #     # @classmethod
# #     def get_species(cls):
# #         print(f"species: {cls.species}")

# #     # @classmethod
# #     def set_species(cls , new_name):       #classMethod || cls refer class 
# #         cls.species = new_name
# #         print(f"Species : {cls.species}")

# # d2 = dog()
# # (d2.get_species()) 
# # d2.set_species("kutta")
# # d3 =dog()
# # d3.get_species()



# # new objest 

# # class dog :
# #     @staticmethod      
# #     def nice_dog():     # static method 
# #         print("bhadiya dog hai bhai")

# # d3 = dog()
# # d3.nice_dog()


# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

# class Developer(Employee):
#     lang="python"

#     def display(self):
#         print(self.name,self.salary,self.lang)

# emp1=Developer("ram",13000)
# emp1.display()
# class Animal():
#     def sleep(self):
#         print("loves sleeping")
# class Cat(Animal):
#     def meow(self):
#         print("meow")

# obj=Cat()
# obj.meow()              
# obj.sleep()

# class Vehicle:
#      def start(self):
#           print("starting vehicle")
        


# class Bike(Vehicle):
#      def ride(self):
#           print("two wheeler ")

# obj=Bike()
# obj.ride()
# obj.start()       
          
# class Employee:
#     name="ram" 
#     salary=13000
#     def show_detail(self):
#         print(self.name,self.salary)
# class Manager(Employee):
#     department="cse" 
#     def manage_team(self):
#         print(self.department) 
# obj=Manager()
# obj.manage_team()
# obj.show_detail()           

# class Shape:
#     def info(self):
#         print("hello")
# class Rectangle(Shape):
#     length=13
#     width=12
#     def area(self):
#         print(self.length*self.width)

# obj=Rectangle()
# obj.info()
# obj.area()

# 
class Employee:
    id="shgfbcuy"
    name="ram"
    salary=1234

class Engineer(Employee):
    def __init__(self,lang,years):
        self.lang=lang
        self.years=years
    def hra(self):
        self.h=0.2*self.salary
        
    def bonus(self):
        if self.years>5:
            self.b=0.1*self.salary
        else:
            self.b=0.05*self.salary
        self.total=self.salary+self.b
    def display(self):
        print(self.id)
        print(self.salary)
        print(self.name)
        print(self.h)
        print(self.b)
        print(self.total)
obj=Engineer("python",2)
obj.hra()
obj.bonus()
obj.display()
