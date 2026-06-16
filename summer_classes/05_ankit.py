        #method Overloading 

# class Area :
#     def area1(self , l=0 , b= 0 , r=0):
#         if l==0 and b==0 :
#             area = 3.14*r*r
#             print(area)
#         else :
#             area = l*b
#             print(area)
        
# a1=Area()
# a1.area1(r=2)

# mehtod 2 

# class Shape :
#     def area(self , a , b=0):
#         if b==0 :
#             return (3.14*a*a)
#         else : return a*b

# a1=Shape()
# print(a1.area(2))
# print(a1.area(2, 3))


        # CAlculator

class Calculator :
    def add(self , *args):
        return sum(args)    # it sum all the integers 
c1=Calculator()
print(c1.add(2,3,4,5,1))



#
class ATM:
    def __init__(self):
        self.pin = ' '
        self.balance =0 
        self.menu()
