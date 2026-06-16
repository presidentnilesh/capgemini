# # khus ka datatype

# class Fraaction:
#     def __init__(self , a , b):
#         self.num = a
#         self.den = b

#     def __str__(self ):
#         return "{}/{}".format(self.num , self.den) 


#     def __add__(self , other):
#         new_num = self.num * other.den + self.den * other.num
#         new_den = self.den * other.den
#         return "{}/{}".format(new_num , new_den) 
    
#     def __sub__(self , other):
#         new_num = self.num * other.den - self.den * other.num
#         new_den = self.den * other.den

#         return "{}/{}".format(new_num , new_den) 
    
#     def __mul__(self , other):
#         new_num = self.num *other.num 
#         new_den = self.den * other.den

#         return "{}/{}".format(new_num , new_den) 
    
#     def __truediv__(self , other):
#         new_num = self.num *other.den
#         new_den = self.den * other.num

#         return "{}/{}".format(new_num , new_den) 

    
# n1 = Fraaction(2,3)
# n2 = Fraaction(4,5)

# print(n1 + n2)
# print(n1 - n2)
# print(n1 * n2)
# print(n1 / n2)


            # lambda is a kind of functon which is use to add , sub and all in jsut 1 line 
# a = lambda x: x**2
# print(a(3))

        # if elae in lambda

gt = lambda a, b : a if a >b else b     # jo print karana hai usko is or rlse ka aage likhna hai 
print(gt(2,3))

even = lambda a : "even" if a%2 == 0 else "odd"
print(even(4))

# create a lambda function to get the last digit of a number 
last = lambda m : m%10 
print(last(254))

two_last = lambda k : k//10 
print(two_last(345))

seven = lambda p : True if p /7 ==0 else False
print(seven(89))