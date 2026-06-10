# date is 06/04/2026 and today is aditya narayan sahu sir's birthday 

# #types of arguments ( arg in function)
## 1. posotional def sum(a,b,c):
# body 
# sum(10,20,30)
## 2. keyword ( we have to pass the value with the cariable name )
# def detail(age, name , add):
#     body 
# detail(afe=27 , add ="jamshedpur" , name="nilu paaji")
# # 3. default argument ( at the time of declariaction , we just have to pass value at the calling time or the default value will ba passed)
# def sum ( a, b, c=12):
#     add=a+b+c 
#     print(add)
# sum(10 , 20)

# # 4. var length or variable length argument 
# def sum(*s):     #type of *s is tuple
#     add=0
#     print(type(s))
#     for i in s :
#         add=add+i
#     print(add)
# sum(1,2,3,4,5,6,8,9,7)

    #wap to pass 13 value during the fuction call and design a function to print only odd numbes from those values 

# def value(*a):
#     for i in a :
#         if i%2!=0 :
#             print(i)
# value(1,2,3,4,5,6,7,8,9,10,11,12,13)

        #packing and unpacking 

# data= 1, 5,32,41,34
# a,b,c,d,e=data
# print(data)

        #global and local variable 

# a=10 
# b=9    #global variable 
# def me():
#     b=12     #local variable
#     print(a)
#     print(b)
# me()
# print(a)
# print(b)

# a=[1,5,2,7,8]
# def m():
#     global a       # global is use it call the a from global and now we can acess it to modify , update or do anything that we want to do 
#     a=[2,2,2,2]
#     print(a)
#     print(id(a))
# m()
# print(a)
# print(id(a))

# wap to print 

def detail(**kwargs):
#     for i in kwargs :
    for key , value in kwargs.items():
        print(key , "-", value)
detail(name = "Vishal" , Address = "Punjab", course =" AIML")
