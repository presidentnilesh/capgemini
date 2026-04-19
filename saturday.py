# sum = 34 + int(34.4) 
# print(sum)
# a =int(53.8)
# print(a)

# m = 2+(4+3j)           # complex number calculation
# print(m)

# st = "345"
# print( 2+ int(st))

# # str = "abh"
# # print( 2 + int(str))    # as stirng can't be added as it is not campatible

# ls = [ 1,2,3,[4 , 39 , 23]]
# # print( 2 +ls)      # now the compiler is confused where he have to add 2 
# ls2 = ls.copy()

# # print(ls )
# # print(ls2)

# ls[2] = 200 
# print(ls)
# ls[1] = 243
# print(ls)
# # if we change original list using .copy , then

import copy
ls = [ 1, 2,3 , [ 200 , 300]]
ls2 = copy.deepcopy(ls)
print(ls)
print(ls2)

ls[1]= 23
print(ls)
ls2[3][1]=345
print(ls2)