


class Student :
    college_name = "cgc"
    course = "cse"
    location = "india"
    def __init__ (self , name , age , gender):
        self.name = name
        self.age = age
        self.gender = gender 
        print("haanji")

ob = Student('Uttam' , 23 , 'male')
print(ob)