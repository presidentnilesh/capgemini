# wap to print each caracter pf a string 
# name = 'nilesh '
# for i in range (len(name)):
#     print(name[i])
# name = "gadha "
# for i in  name :
#     print(i)

#     #wap to reverse a string without slicing or in build function

# name = "nilesh"
# rev = ""
# i = 0
# while i < len(name):
#     rev =(name[i] + rev)
#     i+=1
# print(rev)
# name = " babydoll"
# for i in name[len(name)-1::-1] :
#     print(i)
   
    #or

name = "gadha "
rev = ""
for i in name :
    rev = i + rev 
print(rev)
# or 
# name="anand"
# i = len(name) - 1
# while i>=0 :
#     print(name[i] , end="")
#     i-=1

#             # wap to print lower case character from a string 
# name = "uttam "
# i = 0 
# while i<len(name):
#     if name[i].islower():
#         print(name[i])
#     i+=1

#         #OR 
# name = "Mmummy "
# i = 0 
# while i<len(name):
#     if name[i]>='a' and name[i]<='z' :
#         print(name[i])
#     i+=1

#wap to print captial letter from a string using askais values

# name = "Mmummy "
# i = 0 
# while i<len(name):
#     if ord(name[i])>=65 and ord(name[i])<=90 :
#         print(name[i])
#     i+=1




# wap to print ne string form a old string by extracting only upper case alphabets using askai values and for lopp

# s = "HHi I Am YoUr PyThon TraIner"
# rev=""
# for i in s:
# #     if i>='A' and i<="Z" :
# #         rev=i+rev
# # print(rev)
#     if i.isupper():
#         rev = i +rev 
# print(rev)