

# 1.WAP TO SQUARE AND CUBE EACH AND EVERY ELEMENT IN THE GIVEN LIST
# list_ = [1,2,3,4] ===> out = [[1, 1], [4, 8], [9, 27], [16, 64]]
    # Answer 
# list1 = [1,2,3,4]
# a = list(map(lambda l : [l**2 , l**3] , list1  ))
# print(a)

# # 2.WAP TO GET THE FOLLOWING OUTPUT
# list_ = [56, 8.7, [1,2,4], 'helloo', 9-9j, [1,2,3,4]]
# # out = [1, 1, 3, 6, 1, 4]

    # answwer
# o = list(map(lambda i : len(i) if hasattr(i, "__len__") else 1 , list_ ))
# print(o)

# # # 3.WAP TO GET THE FOLLOWING OUTPUT
# stri = 'hii hello how are you'
# str = stri.split(' ')
# o = list(map(lambda p : len(p) , str))
# print(o)
# # out = [3, 5, 3, 3, 3]

# # 4.CONVERT LIST OF STRINGS TO UPPERCASE
# list_ = ['Hello', 'hii', 'how are you']

# # 5.CONVERT LIST OF STRINGS TO INTEGERS
# list_ = ['1', '2', '34', '4567', '56789']

# # 6.ADD TWO LISTS ELEMENT-WISE USING Zip()
# a = [1, 2, 3]
# b = [4, 5, 6]

# # 7.WAP TO GET THE FOLLOWING OUTPUT
# LIST_ = [123, 34, 24, 512]
# a = list(map(lambda n : sum(map(int , str(n))) , LIST_))
# print(a)
# # OUT = [6, 7, 6, 8]

# # 8.STRIP WHITESPACE FROM STRINGS
# raw_strings = ['  apple  ', ' banana ', 'cherry  ']    # out =  ['apple', 'banana', 'cherry']
# t = list(map(lambda i : i.strip() , raw_strings ))  #strip function is use to trim all the exxtra space 
# print(t)

# # 9.PREFIX EACH ITEM WITH ITS INDEX USING ENUMERATE
items = ['apple', 'banana', 'cherry']
o = list(map(lambda i : (i[0] , i[1]) , enumerate(items)  ))    #enumerate() is a built-in function that gives index number + value from a collection.
print(o)
# ## out = {0: 'apple', 1: 'banana', 2: 'cherry'}

# # 10.COUNT_VOWELS  USING A LAMBDA FUNCTION AND MAP.
# # Input
words = ["hello", "world", "python", "programming"]

# # Output [2, 1, 1, 3]

# # 11.CONVERT A LIST OF STRINGS INTO A LIST OF DICTIONARIES WITH KEYS
# words = ["hello", "world", "python", "programming"]

# # 12.WAPT FIND IF A GIVEN LIST OF STRING STARTING WITH 'aA'
# names =['Alex','steve','Anna','henry','john']

# # 13.WAPT RETURN A LIST OF ELEMENTS RAISED TO THE POWER OF THIER INDICES
# nums = [1,2,3,4]

# # 14.WAPT CALCULATE THE SUM OF ONLY POSITIVE NUMBER OF A GIVEN LIST
# nums = [1,-8,-3,4,-7,-12]

# # 15.REPLACE NUMBERS GREATER THAN 50 WITH "HIGH" ELSE "LOW"
# nums = [10, 55, 40, 80, 30]


# # FILTER

# # 1.WAP TO EXTRACT ALL THE STRINGS FROM THE TUPLE

# # 2.WAP TO EXTRACT ALL THE INTEGER NUMBER FROM THE COLLECTION ONLY IF THE NUMBER HAVING 3 DIGITS

# # 3.WAP TO GET ALL THE PALINDROME NUMBERS IN THE RANGE 10 TO 100

# # 4.TAKE A LIST OF STRING INPUT, CREATE A NEW LIST WHICH CONSISTS OF ONLY THE EVEN LENGTH STRING


# # 5.FILTER STRINGS THAT ARE ALL LOWERCASE.
# list_ =['hello', 'WORLD', 'Python']

# # 6.FILTER STRINGS THAT START WITH A VOWEL.
# list_ =['apple', 'banana', 'orange']

# # 7.FILTER STRINGS THAT END WITH 'ING'.
# list_ =  ['playing', 'read', 'singing']

# # 9.FILTER PEOPLE OLDER THAN 18
# people = [{'name': 'Tom', 'age': 17}, {'name': 'Anna', 'age': 21}]

# # 10.FILTER BOOK TITLES WITH "PYTHON"
# books = ['Learn Python', 'Data Science', 'Python Cookbook']

# # 11.FILTER VALID PHONE NUMBERS (10 DIGITS)
# numbers = ['1234567890', '98765', '123456789a']

# # 12.FILTER MOVIES RATED > 8
# movies = [{'title': 'Inception', 'rating': 8.8}, {'title': 'Cats', 'rating': 4.2}]

# # 13.FILTER VALID PHONE NUMBERS (10 DIGITS)
# numbers = ['1234567890', '98765', '123456789a']

# # 14.FILTER MOVIES RATED > 8
# movies = [{'title': 'Inception', 'rating': 8.8}, {'title': 'Cats', 'rating': 4.2}]

# # 15.FILTER STRINGS THAT START WITH A VOWEL.
# list_ =['apple', 'banana', 'orange']