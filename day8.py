# hello world i am here ti say you that i can be everythig but i can't be the one wo can be the one 

# start = 1 
# while start <= 10 :
#     print("name ")
#     start += 1 
# print(start)

# num = 3
# while num <= 37:
#     if num % 2 == 0:
#         print(num)
#     num += 1


# # question 2
# num = int(input("enter any natural number till where you want to add"))
# n = 1
# sum = 0
# while n <num+1 :
#     sum = sum + n
#     n = n+1
# print(sum)

# # wap to print sum of odd n natural numbers 

# num = int(input('enter n till where you want to sum naural number ')) 
# sum = 0 
# i = 1 
# while i<= n :
#     if i %2 == 1 :
#         sum += 1 
#         i += 1 
# print(sum )


#divisible by 3 and 5 from 5 to 13

# num = 3 
# while num<= 13 :
#     if num %3 == 0 and num %5 == 0 :
#         print(num)
#     num += 1 

#     # num if digits prenent in a number 
# num = 54321
# while num >0 :
#     digit = num %10 
#     print(digit)
#     num=num//10

#     # wap to print sum of the digits give in a number 
# num = 3264
# sum =0 
# while num >0 :
#     digit = num %10 
#     sum = sum + digit 
#     num=num//10
    
# print(sum)

# # wap to check if a number is prime or not 
 

n = int ( input("enter any number "))
c = 0
i = 1 
while i<=0 :
    if n %i ==0 :
        c+= 1 
    i=i+1
if c==2 :
    print("prime")
else :
    print("not prime")    



    # OR 
n = int ( input("enter any number "))
is_prime =True 
i = 2 
while i<n :
    if n % i == 0 :
        is_prime =False 
        break 
    i += 1 
if is_prime :
    print("prime")
else :
    print("Not prime ")

# to count no of digit present in a number

num = 3264
count =0 
while num >0 :
    count = count + 1 
    num=num//10
    
print(count)
    