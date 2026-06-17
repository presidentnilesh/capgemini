# Question 1: Add Two Boxes (Operator Overloading)
# Problem Statement
# Create a Box class with a weight attribute and overload the + operator to add the weights of two boxes.

    #
# class Box :
#     def __init__(self , weight ):
#         self.weight = weight

#     def __add__(self , other):      #method overloading 
#         return (self.weight + other.weight) # here other.weight denote the weight of other object and self.weight denote the weight of box1
    
    
    
# #creating object 
# box1 = Box(20)
# box2 = Box(10)

# # #adding box 1 and box 2 
# # box3 = box1 + box2

# print("total weight :" , box1 + box2)


# Question 2: Compare Students (Operator Overloading)
# Problem Statement
# Create a Student class with a marks attribute.
# Overload the > operator to compare the marks of two students.

# class Student :
#     def __init__(self , marks1):
#         self.marks1 = marks1

#     def __gt__(self , other):
#         return self.marks1 > other.marks1
    
# s1 = Student(78)
# s2 = Student(70)

# if s1 > s2 :
#     print("Student1 scored greater marks . ")

# else  :
#     print("Student2 has scored greater marks .")



# Encapsulation Examples:-

# Question 1: Student Information System
# Problem Statement
# Create a Student class with private variables:
# __name
# __age
# Create getter methods to retrieve both values and setter methods to update them.
# Operations:
# Display name and age.
# Change the age.
# Display updated details


# class Student :
#     def __init__(self , name , age ):
#         self.name = name 
#         self.age = age 

#     #getter
#     def get(self):
#         print("the name is :" , self.name)
#         print("the age is :" , self.age)

#     #setter 
#     def set(self , age):
#         self.age = age
    
# s1 = Student("Nilesh" , 22)

# s1.get()
# s1.set(24)
# s1.get()


# EXAMPLE 2 : Digital Wallet System
# Problem Statement

# Create a DigitalWallet class with private variables:

# __wallet_id
# __balance
# __transaction_limit

# Private Methods:

# __validate_amount()
# __check_limit()

# Public Methods:

# add_money()
# send_money()
# check_balance()
# transaction_history()

# Conditions

# Amount must be positive.
# Transaction should not exceed the limit.
# Balance should never become negative.


class DigitalVariable :
    def Options(self , wallet_id , balance , transection_limit):
        self._wallet_id__ = wallet_id
        self._balance__ = balance 
        self._transection_limit = transection_limit 
        self.__history = []

    def __valid_amount__(self , amount):
        if amount < 0 :
            return False 
        else : True

    def __check_limit(self , amount):
        if amount <= self._transection_limit :
            return True
        else :
            return False
    
    def add_money(self , amount):
        if self.__valid_amount(amount):
            self._balance__ += amount 
            self.history.append()
            print("Money added successfully !")

        else :
            print("Invalid amount")
        
    # def send_money(self , amount ):
    #     if 



    # def transaction_history()