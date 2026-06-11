# iAbstraction 

# class car :

#     def __init__(self):
#         self.acc = False 
#         self.clutch = False
#         self.brk = False
     
#     def Start(self):
#         self.acc =  True
#         self.clutch = True
#         self.brk = True
#         print("Car has Started..")

# c1 = car()
# c1.Start()


    #question 

class Account():
    print("welcome ...")

    @staticmethod
    def account():
        print("Your account number is : 2762426788")
    
    def __init__(self , acc  , balance):
        self.account = acc 
        self.balance = balance 

    #debit method 
    def credit(self , amount):
        self.balance += amount
        print("RS.", amount , " is credited.")
        print("final amount is :" , self.get_balance())

    def debit(self , amount):
        self.balance -= amount 
        print("RS." , amount , "was cradited" )
        print("final amount is :" , self.get_balance())

    def get_balance(self):
        return self.balance
    

acc1 = Account(23746274 , 10000)
print(acc1.balance)
print(acc1.account)
(acc1.debit(300))
acc1.credit(500)