# # generator : generator are simple way of generating/creating iterator 

# def abc(a):
#     sum = a + 10 
#     multiply = a **3
#     yield sum   # it is use to return the address of the object 
#     yield multiply  # we can not use eturn word for two times but we ca use yield for many times 
                        ## by yield we dont have to woorry about the break statement ...a
  
# p = abc(10)

# for i in p :
#     print(i)


# demo 
# def gen_demo():
#     yield "hi. baby"
#     yield "runn"
#     yield "dooro"
#     yield "bhagoooo"

# p = gen_demo()
# for i in p :
#     print(i)


    #example 

# def sq(num):
#     for i in range(1 , num+1):
#         yield i**2

# m = sq(5)

# for i in m :
#     print(i)


# def one_to_ten() :
#     n = 1 

#     while n <=10:
#         yield n 
#         n=n+1 
#         # print(n)
# num = one_to_ten()
# for i in num :
#     print(i)


#question 1 : create a generator that generates numbers from 1 to 5 and display them using a for loop 
# def nums():
#     for i in range(1 , 6):
#         yield i 
# p = nums()
# for o in  p :
#     print(o)


# question : create a generator that generateas even numbers from 2 to 10
def even():
    for i in range (0 , 11):
        if i %2 == 0 :
            yield i
r = even()
for q in r :
    print(q)