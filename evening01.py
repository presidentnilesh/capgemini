# num = int (input("enter any number"))
# i = 2
# while i < num :
#     if num%i == 0 :
#         print("the number is not a prime ")
#         break
#     else  : 

                                # print("the number is not prime .


        # linear search 
# arr = [ 5,1,3,4,6]
# i = 0
# while i< len(arr) :
#     if arr[i] == 3 :
#         print("3")
#     i+=1 


                                 #reverse a list using while loop

# ls = [ 1,2,3,4,5]
# ls2 = []
# i =len(ls)-1     # i did a dsingle mistake , i have taken  = 1- len(ls)
# while i >=0 :
#     print(ls[i]) 
#     ls2.append(ls[i])
#     i = i-1
# print(ls2)


                                #remove dublicates element from list without using set and find common elements .
# ls =[1,1,3,4,5,2,3,6,2,5,2,4,5,2,5,2,4]
# i = 0 
# while i < len(ls) :
#     j = i+1 
#     while j < len(ls) :
#         if ls[i] == ls[j] :
#             ls.pop(j)
#         else :
#             j+=1 
#     i=+1     
# print(ls)

ls = [ 1,2,3,1,2,3,2,4,5,2,5,2,5,6,8,3,3,2,5,2,4,5,3,1,2,5,2,5]
i = 0 
while i<len(ls) :
    j=i+1 
    while j<len(ls) :
        if ls[i] == ls[j] :
            ls.pop(j)
        else :
            j+=1 
    i+=1 
print(ls)
            




   # merge two list using while loop
   # count frequency of each character in list 
   # fund the second largest element in a list 
# ls = [ 2,4,6,76,4,7,4,47,8,4,57,8]

