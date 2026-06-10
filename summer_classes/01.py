# print("hello world !")

# inp = "techincal"
# count = 0 
# for num in inp:
#     if num == "a" or num == "e" or num == "i"or num == "o" or num == "u" or  num == "A" or num == "E" or num == "I" or num == "O" or num == "U" :
#         count += 1  
# print(count)



# nil = "abcde"
# for i in range(1, len(nil) ,2):
#     print(nil[i])


# set = [ 1 ,2, 3]
# setn=[]
# for i in range(len(set)-1 , -1 , -1) :
#     setn.append(set[i])
# print(setn)


# pho = [ 1,2,0,4]
# for i in range(len(pho)-1) :
#     if pho[i] == 0 :
#         pho.pop(i)
# print(pho)

# wap. to check palindrom or not ?
# wap to count the number of upper case and lower case letter un a string 
# wap to print fibonacci series 
# wap to print characters at even index 

num1 = 1331
original = num1
rev = 0 
while num1 > 0 :
    digit = num1 % 10 
    rev = rev* 10 + digit 
    num1 = num1 // 10 
if original == rev :
    print("its pallindrom ")
else : 
    print("its not pallindrom")


#. wap or a leap year 

year = int(input("enter the year"))
if (year %400 == 0 ) or (year % 4 == 0 and 100 % 100 != 0) :
    print("it's leap year ")
else : ("print its not ")