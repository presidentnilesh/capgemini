# list 
a = [ 1, 2 ,3 ]
a[1] = 200          #list is a mutable datadtype ( it can be change) and it is alos know as unhashable datatype 
print(a[1])


# method in list 
ls = [1,2,3]
ls.append(4)          # it is use to add any elements in the end of the list , it only take only one argument .
print(ls)

# ls.append(5,6)
ls.extend((5,6))        # it is use to pass the value in collection and use this in bracket.
print(ls)

ls.pop()            # it remove the last value as value is not given , so it will take the value as -1 .
print(ls)
ls.pop(3)       # it remove the given element 
print(ls) 

b = ls.copy()          # it copy the list ls
print(b , "a")
ls.pop(2)      # it remove the element whichi is in index 2
print(ls)


print(ls.count(5))            # it count the number of occurance 

print(ls.index(5))       # it give you the index in which 5 is prensnt 
ls.remove(1)         # it remove the specified number from the list 
print(ls)

ls.extend(( 2, 4 , 7, 6, 9))
print(ls)

# list in list 

m = [ 1,2,3,[4,5]]
print(m[3][1])

# ls.clear()      # it is use to clear all the elements of list 
# print("mn = ", ls)

# tuple -> it is the collection of homogeneous and heterogeneous valuse inclosed between ()
# it is an immutable datatype or hashable datatype  . its standard value is () 

# print(dir(tuple))

t = ( 1 ,2, [1,2,3])
t[2][1] = 200     # to change the elemrnt of lis which is in touple .
print(t)



# print(dir(list) )

print(m + ls)       # it join or add both list

# set  : it is mutable collection and unoedered collection of values immutable values . it keeps ony unique element . indixing and slicing is not present . every single value of datatype is imutable datatype .. 

# set representation - > set()

s = { 1,2,3,4,5 , ' abcd'}
print(s)

# add function : it add the  and s.pop( ) -> it remove the first element of set .
(s.pop())          # we cannot pass any element , it only remove the 1st element of set 
print(s)
# s.clear     it remove all the element of the set 

# s.remove(2)      -> it remove the element which is passed in the remove function 
# discard function -> s.dicard(2)      if any value is pased which is not present in the set , it will not pass any error 
