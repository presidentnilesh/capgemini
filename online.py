# class car :
#     brand = "none" 
#     color = "none"
#     def start():
#         print("sttrted")
# obj1 = car()

# car.start()
# obj1.start()        # this is wrong , as 

class bank():
    bank_name = "SBI"
    branch = "Dimna"
    code = "SBIN001188"
    country = "India"

    def details ( name , age , phone , pan , address ):
        bank.name = name 
        bank.age = age 
        bank.phone = phone 
        bank.pan = pan 
        bank.address = address 

c1 = bank()
c1.details(('adi', 26 , 9798 , 'india' ))

class bank :
    branch = 'sbi'
    ifsc = 'sbin000123'

    def __init__ (self , name , age , phone ):
        c1 = bank('adi', 25 , 9798)


        