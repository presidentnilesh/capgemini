# 1.⁠ ⁠WAP TO READ A TEXT FILE AND PRINT ONLY THE LINES THAT CONTAIN THE WORD "PYTHON".
# Example file:
# file.txt
# I love Python
# Java is also popular
# Python is easy

# with open ('gujju.txt' , 'w') as g :
#     g.writelines("Ilove her .\n she is very preety \n i love her tiny or small nose .")
#     g.close()

    # 2. WAP TO READ A FILE AND PRINT ONLY THE LINES WHOSE LENGTH IS GREATER THAN 20 CHARACTERS.

# with open ('gujju.txt' , 'r') as g :
#     for line in g :
#         if len(line)>=20 :
#             print(line)
#     g.close()

# 3.⁠ ⁠WAP TO COUNT THE NUMBER OF VOWELS PRESENT IN A TEXT FILE

# with open ('gujju.txt' , 'r') as g :
#     count = 0 
#     for line in g : # it wwill run the loop in the lines 
#         for ch in line :    # it will run the loop oin the alphabets 
#             if ch in "aeiouAEIOU" :
#                 count += 1 
#     print(count)
# g.close()

# 4.⁠ ⁠WAP TO READ A FILE AND EXTRACT ALL THE INTEGER NUMBERS HAVING EXACTLY 3 DIGITS.

with open ('gujju.txt' , 'r') as f :
    for line in f :
       words = line.split()

       for num in words :
           if num.isdigit() and len(num)==3 :
               print(num)
        
        