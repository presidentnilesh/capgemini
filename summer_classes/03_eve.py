class user :
    def __init__(self , name):
        self.name = name 
        print("main entry la chuka hoon")

    def login(self):
        print("successfully login with" , self.name)
    

class Student(user):        #instructor can also inherit by child from parent 
    pass




# parent = user()
# parent.login()

# child = Student()
# user1 = user()

# child.login()
# child.enroll()

# print(child.a)
# print(user1.a)

# print(child.b)
# print(user1.b)        // user1 can't access child as user1 is the chils and child is parent .. and parent can;t access parent class

st1 = Student("yash")
st1.login()


        # what gets inherit ?
        # * COnstructor (__init__)
        # * Non Private Atributrs
        # * Non Private Methods