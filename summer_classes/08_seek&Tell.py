# seek during write

# f = open("s2.txt" , 'w')
# f.write("hi\n hello \n byr\n kaiashe hia aap \n")
# f.close()


# f = open('s2.txt' , 'r')
# print(f.read(2))
# print(f.tell())
# print(f.read(3))
# print(f.tell())
# print(f.seek(0))

# print(f.read(2))
# print(f.seek(8))
# print(f.read())

# take input in a list using file handling 
# f= open('s3.txt' , 'w')
# f.write(" [1,2,3,4,5,6,7,8,9,10]")
# f.close()
 
# list-comprehension

# a = [ i**2 for i in range(10) if i %2 == 0 ]    #jaishe sign hamlog denga waishe he type cast khud sha ho jayega 
# b = { m : m**2 for m in range (14) if m%3 ==0 }
# print(a)
# print(b)

# write lines
# L = ['chips\n', 'soda\n', 'easyday']
# f = open('sample.txt', 'a')
# f.writelines(L)
# f.close()
with open('sample.txt', 'r') as f:
  print(f.read(7))