# ls=[20,10,30,40,50,10,20]
# target = 100
# for i in range (0, len(ls)):
#     if ls[i]== target :
#         print('element found at index :' , i)
#         break 
# else : print("element is not found")


# ls = [10,20,30,20,10]
# target = 20 
# is_found = False 
# for i in range(len(ls)) :
#     if ls[i] == target:
#         print(i)
#         is_found = True
# if not is_found :
#     print("number not found ")

    # find largest number from given list 

# ls= [1,2,3,4,5,3,2,4,2]
# largest = ls[0]
# for i in range (len(ls)):
#     if ls[i] > largest :
#         largest = ls[i]
# print(largest)

#        # OR 
# ls= [1,2,3,4,5,3,2,4,2]
# largest = ls[0]
# for i in ls :
#     if i > largest :
#         largest = i
# print(largest)

#. nested loop 

# for i in range(3) :
#     print("*" , end=' ')

# #
# for i in range(3):
    
#     for j in range(3):
#         print("*", end=" ")
#     print()


    # remove duplicate values from list 

# ls=[ 1,2,1,1,2,4,1,2,6,1,2,4]
# for i in ls :
#     for j in range(len(ls)-1 , i , -1):
#         if ls[i]==ls[j]:
#             ls.pop(j)
#         else : j+=1
#     i+=1
# print(ls)
        


        # function wih return and without args

# syntax :  def function():
            #     tatement Block 
            #     return val 
            # fun_name() <-- fun calling 
    
def uppercase():
    st=input("enter a string") 
    st=st.upper()
    print (st) 
print(uppercase())
print(type(uppercase))

# funtion with args and rreturn 

