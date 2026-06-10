ls =[1,1,3,4,5,2,3,6,2,5,2,4,5,2,5,2,4]
l= []
i =0 
while i<(len(ls)) :
    if ls[i] not in l :
        l.append(ls[i])
    i+=1

print(l)


# wap to count spy numbers given in a list 
ls = [1124 , 123 , 141 , 22, 31, 213 , 64 , 21 ]
i = 0
sum = 0 
pro = 1
while i<len(ls) :