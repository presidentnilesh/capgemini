d ={ 'a': 2 , 'b' : 3 , 'c': 4 , 1 : [ 1,2,3,]}
print(d)
print(type(d)) 
print(d.get('aaaa' , "key is not found"))        # we use get so that if i etere an key whch is not present , it will not pass an error 
print(d['a'])

print(d.keys())     # it gives all the key names

print(d.values())          # pass all the values 

print(d.items())        # pass alll the items ( key and the values)

print(d.popitem())       # it remoe tthe last item of the distionary

print(d.pop('a'))       # it remove the specific keyvalue which we will pass in the code

d['asad'] = 12333       # it add the new item and value in the dist


print(d)

d['cgc'] = 111 
print(d)
d['cgc'] = 121 # it update the key value of the dist
print(d)

# dist is a mutable but its key is immutable and it's value can be mutable
# copy operation -> 1. General copy 2. Shallow copy 3. Deep copy 
#
