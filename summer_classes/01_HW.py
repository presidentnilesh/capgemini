#create  CLASS CALLED STUDENT 
#  Requirements 
#create clas member 
#college_name
#courses
#location 
#No. of hostel 

class Student :
    name = " NIlesh " 
    roll = 1234 
    subject = "CSE" 
    def show(self):
        print(self.name , self.roll , self.subject)
s1 = Student()
s1.show()