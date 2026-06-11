# class Student():
#     college_name = "CGC"

#     def __init__(self , name , course , marks):
#         self.name = name 
#         self.course = course
#         self.marks = marks
#         print(f"Name is {self.name}  \nCourse is {self.course}")

#     def welcome(self):
#         print("Welcome to India.")

#     def get_marks(self):
#         print("your marks is ," , self.marks)

# s1 = Student("Pronay" , "CSE" , 87)
# s1.welcome()
# s1.get_marks()
# print("----------")
# s2 = Student("Kanishk" , "AIDS" , 89)
# s2.welcome()



# question 2 

class Student():
    def __init__ (self , name , sub1 , sub2 , sub3 ):
        self.name = name 
        self.sub1 = sub1 
        self.sub2 = sub2
        self.sub3 = sub3
    @staticmethod
    def hello():
        print("hello" )
    def avg(self):
        print("avg of all subjecct marks is :" , (self.sub1 + self.sub2 + self.sub3 )/3 )

s1 = Student("Knaishk" , 80 , 82 , 87)
(s1.hello())
(s1.avg())
