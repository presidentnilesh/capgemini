# read function
# l =['cgc\n' , 'CSE cd\n' , 'dumb\n' , 'stdents']
# with open("sample.txt" , 'w') as f :
#     f.writelines(l)


# with open('sample.txt' , 'w') as f :
#     f.writelines(l)


# f = open('sample.txt' , 'r')
# while True :
#     data_f = f.readline()

#     if data_f == '':
#         break 
#     else :
#         print(data_f)
# f.close()


# benifit -> to load a bog file data in memory 
large_data =['so rahi ho kya hai ?' for i in range (1000)]
print(large_data , end=' ')

with open ('large_data.txt' , 'w' ) as f :
    f.writelines(large_data)

with open('large_data.txt' , 'r') as f :
    chunk_size = 100 

    while len(f.read(chunk_size)) > 0 :
        print(f.read(chunk_size) , end=' ')

        f.read(chunk_size)

        