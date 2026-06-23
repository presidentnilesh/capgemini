# hand made iterator 
# 
# 
# # def khud_ka_loop(collection):
#     iterator_collec = iter(collection)

#     while True:
#         try:
#             print(next(iterator_collec))
 
#         except StopIteration:
#             break 

# a= [1,2,3,4,56,3,6]
# b = "namaste"
# c =(1,2,3,4,5,6)

# print(a)


class one_to_ten :
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.num <=10 :
            val = self.num 
            self.num += 1 
            return val
        else :
            raise StopIteration
        

n = one_to_ten()

for i in one_to_ten():
    print(i)

