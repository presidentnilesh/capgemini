# class A :
#     aa = 10 
#     b=20
#     @classmethod
#     def display(cls):
#         print(cls.a , cls.b)

#     class B(A):
#         c=30 
#         def __init__(self, m):
#             self.m = m 

#         def display2(cls):
#             print(cls.c) 
#     obj2 = B(20)
#     B.display()
#     obj2.display2()



class Bank ():
    bname = "sbi"
    branch = "mango"

c1 = Bank()
c1.name = "nothing"
c1.mno = 48573457




class Bank :
    bname = 'SBI'
    branch = 'mango'

    def details (obj , name , mno):
        obj.name = name 
        obj.mno = mno 
        