f = open("student.txt" , 'w')
f.write("kaishe hai aap baby ji ?")
f.close()

f = open("student.txt" , 'a')
f.write("\nnaraj ho kya aap ?")
f.close()

with open('student.txt' , 'a') as f :
    f.write("\nkaishe ho babay , bataoo na aap , itna bhi kya naeraj hoona ... mera samne mera dost baatha hai sayad usko sak ho jayega , to aap jaldi bataoo na ")
    f.close()

with open ('student.txt' , 'r') as f :
    print(f.readline() , end="")
    print(f.readline() , end="")
    print(f.readline() , end="")
    
    
