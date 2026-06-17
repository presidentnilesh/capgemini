#. Map() -> it is use to apply a function to every element of a collection (list, tuple, etc.) without writing a loop.

# L = [ 1,2,3,4] 
# m = list(map(lambda x : x**2 , L))
# o = list(map(lambda x : x*5 , m))
# print(m)
# print(o)

#example two

# l = [[1,1], [2,4] , [3 , 9]]  # question was wrong 

# a=list(map(lambda x : [ x , x**2] , l ))
# print(a)


# a = 'haanji'
# a=a.upper()
# print(a)

# st = [ 'hello ' , 'baby' , ' kaishe' , ' hai']
# m = list(map(lambda x : x.upper() , st))
# print(m)

# covert list of string to integer

# list = [ '1' , '312' , '34' , '342' ,'4253']
# p = list(map(lambda x : int(x) , list))
# print(p)


# wap to get rhe following output 
# s = 'hi hello how are you'
# l1 = s.split(' ') # use to split when there is space
# list = list(map(lambda x : len(x) , l1 ))
# print(list)


            #filter()

#syntax : filter(lambda x: condition , collection)

#question 1 : filter only those are greater then 3 
l = [ 3,1,5,20 , 3, 0]
a =list(filter(lambda x : x>3 , l))
print(a)

#question 2 : filter even number 
e = [2,4,5,7,9,94]
o = list(filter(lambda y : y%2 == 0 , e))
print(o)

# question 3 : filter words longer then 3 characters

u = [ "hi" , " hello" , "super" , "sellow"]
w = list(filter(lambda c : len(c)>=3 , u))
print(w)

# question 4 : filyter strings starts with 'a'

z = [ 'apple' , 'mmango', 'banana' , 'papaya']
q =list(filter(lambda t : t.startswith('a') , z))   #startswith
print(q)


