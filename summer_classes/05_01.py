#  question 1 :
# Create a Calculator class with an add() method that can:
# Add 2 numbers
# Add 3 numbers
# Add 4 numbers

# class Calculator :
    

#     def add2(self  , a , b):
#         sum = a + b 
#         print(sum) 
#     def add3(self  , a,b,c):
#         sum = a+b+c
#         print(sum)
#     def add4(self , a,b,c,d):
#         sum = a+b+c+d
#         print(sum)

# add=Calculator()
# add.add4(1,3,2,3)
# add.add2(3,4)



# using another method 

# class Calculator :
#     def add4(self,a,b,c=0,d=0): #default parameter of c and d is equal to 0 . so if i dont give the value of c and d it will assign it to 0 
#         sum = a+b+c+d
#         print(sum)

# add=Calculator()
# add.add4(1,3,2,3)
# add.add4(3,4)



# Question 2: Student Details (Method Overloading)
# Problem Statement
# Create a Student class with a display() method that can: 
# Display only the student's name 
# Display name and age 
# Display name, age, and course

# class Student :
#     def N(self , name):
#         self.name = name 
#         print(name)
    
#     def NA(self , name , age ):
#         self.name = name 
#         self.age = age 
#         print("name is :" , self.name)
#         print("age is :" , self.age)
#     def NAC (self , name , age , course):
#         self.name = name 
#         self.age = age 
#         self.course = course 
#         print("name is :" , self.name)
#         print("age is :" , self.age)
#         print("courseis :" , self.course)

# stu=Student()
# stu.N("anand")
# stu.NA("anand" , 23)
# stu.NAC("anand" , 23 , "Law")


        # method 2 

class Student :
    def N(self , name):
        print(name)
    def NA(self , name , age ):
        print("name is :" , name)
        print("age is :" , age)
    def NAC (self , name , age , course):
        print("name is :" , name)
        print("age is :" , age)
        print("courseis :" , course)

stu=Student()
stu.N("anand")
stu.NA("anand" , 23)
stu.NAC("anand" , 23 , "Law")



# Question 3: Area Calculation (Method Overloading)
# Problem Statement
# Create a class Area with a method calculate_area() that can: ,
# Calculate the area of a square , Calculate the area of a rectangle ,
# Calculate the area of a triangle

