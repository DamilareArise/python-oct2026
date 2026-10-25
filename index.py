# print(20 + 20)
# print("Welcome to class Elijah")

""" 
qwerty qwerty qwerty
qwerty qwerty qwerty
"""

# print("Hello")

# def welcome():
#     print("You are welcome")
    
# Python variables
# variable name, assignment operator, value

name = "Elijah"
basket = "Apple"
number = 60

# print(basket)
# basket = "Orange"
# print(basket)

# rules guiding variable declaration 
# 1. a variable does not contain spaces only alphabet, number and underscore
first_name_of_the_student = 'Ifeoluwa'  # snake
# firStNameOfTheStudent # camel
# FirstNameOfTheStudent #pascal

# 2. You can not start a variable name with a number
# _2nd_day = 
# 3. Variable name should be descriptive 
# student_name = "Ayomide"

# Types of variable declaration 
# 1. single variable, single value 
student_name = "Ayomide"
# print(student_name)

# 2. single variable, multiple values 
students = "Michael", "Anne", "Jerry"
# print(students)

# 3. multiple variable, single value
# a = b = c = 10
# a = 10
# b = 10
# c = 10

b = 20
# print(a) 

# 4. multiple variable multiple values
ade, bola, ola = 20, 10, 10
# print(ola)

# concatenation: joining two or more strings

username = "Damilare"
course = "Python"
duration = 2
duration_unit = "months"

# print("Welcome, " + username + ". This is " + course + " class. Its for " + str(duration) + duration_unit )

# fullname = input("Fullname: ")
# age =  int(input("Age: "))

# print("My name is " + fullname + ". I am " + str(age) + "Years old")

# print("My name is", fullname , ". I am " , age , "Years old")

# f-string
# print(f"My name is {fullname}. I am {age}years old")

# fullname = input("Fullname: ")
# print(fullname)


# value1 = int(input("Value1: "))
# value2 = int(input("Value2: "))
# print(value1 + value2)



# Python datatypes
# 1. Number type: int, float, complex
num = 45
num2 = 45.5
num3  = 2 + 3j
# print(type(num2))

# 2. Text type: strings
text = "It's mine"
# print(type(text))

# 3. Sequence Type: list, tuple, range
my_tuple = ('bag', 'shoes', 'cloth')
# print(type(my_tuple))
my_list = ['bag', 'shoes', 'cloth']
# print(type(my_list))

numbers = range(1, 21, 2)
# print(list(numbers))

# 4. Boolean Type: True, False
is_active = True
# print(type(is_active))

# 5. Mapping Type: Dictionary
student = {
    "fullname": "Temi Tayo", 
    "course": "AI", 
    "age": 20,
    "address": {
        "city": "Ikeja",
        "state": 'Lagos State',
        "country": "Nigeria"
    }
    }


# print(student["fullname"])
# print(student["age"])
# print(student['address']['city'])

# 6.  Set Type 
# my_set = {'bag', 'shoes', 'cloth'}
# print(my_set)

setA = {3, 5, 6, 7, 2, 2, 1, 8, 4, 9}
# print(setA)

# 7. None Type
val1 = None
# print(val1)

# 8. binary type; bytes, bytearray, memoryview

# print(float(45))
# print(int(45.5))

# str(42) # "45"
# int("2")



# python operators.

# 1.  Arithmetic Operator: +, - , *, /, //, %
# print(5 % 2)

# 2. Assignment operator: =, +=, -=, *= , etc.
var = 2
# var += 2 # var = var + 2
# print(var) 

# 3. comparison operator: ==, !=, >, <, >=, <=
# print(var <= 2)

# 4. Logical operator: AND, OR, NOT
""" 
A       B       AND     OR      NOT A    XOR
0       0       0       0       1         0
0       1       0       1       1         1
1       0       0       1       0         1
1       1       1       1       0         0

"""
# email = True
# password = False

# email = 1
# password = 0

# email = "dami@gmail.com"
# password = None

# print(email and password)

# 5. Membership operator:  in, not in

students = ['Michael', "Anne", "Al-ameen", "williams"]
# print("Ayomide" in students)
# print("michael" not in students)
var = 6
# if var in range(1, 6):
#     print("Yes oo")
# else:
#     print("No eeh")
# "d" in "dami"

# email = input("Email: ")
# if "." in email and "@" in email:
#     print("Email is valid")
# else:
#     print("Invalid email")

# 6. identity operator: is, is not
var2 = 6
# print(var is var2)


# 7. bitwise operator: 
""" 
& - and
| - or
^ - xor
~ - not


2 | 10
    5  r 0
    2  r 1
    1  r 0
    0  r 1
    
    10100
     1010
    00000
"""
# print(bin(20))   
# print(bin(10))   
# print(10 ^ 20)


    
# conditional statement (if/else statement)

# var = float(input("Your Value: "))
# if var == 2:
#     print("Yes ooo")
# else:
#     print("No eeh!")  
    
# if var >= 1 and var <= 5:
#     print("Yes ooo")
# else:
#     print("No ehh")


# below minimum wage, minimum wage, above minimum wage

# minimum_wage = 70000

# salary = float(input("Salary: ") or 0 )

# if salary > 0 and salary < 70000:
#     print("Below minimum wage")
# elif salary == minimum_wage:
#     print("Minimum wage")
# elif salary > minimum_wage:
#     print("Above minimum wage")
# else:
#     print("Invalid value")

# 70-100 A
# 60 - 69 B 
# 50 - 59 C
# 44 - 49 D
# 40 - 44 E
# 0 - 39 F

# Nested if/else

# USSD - system
# *312#

# ussd = input("USSD: ")
# if ussd == "*312#":
#     print("""
#        1. Buy Data
#        2. Check Balance
#        #. Exit 
#     """)
#     choice = input("Choice: ")
#     if choice == "1":
#         print("""
#         1. Daily plan
#         2. Weekly plan
#         3. Monthly plan     
#         """)
#         choice = input("Choice: ")
#         if choice == "1":
#            print("Daily Plan")
#         elif choice == "2":
#             print("Weekly")
#     elif choice == "2":
#         print("Your balance is ***** ")
#     elif choice == "#":
#         exit("Goodbye!")
        
#     else:
#         print("Invalid option.")
     
# else:
#     print("Invalid ussd code")
    
    


# Python Strings


# Assignment: Build a simple CBT application

# print("1. what is the capital of Osun state. a. Osogbo b. Ilorin")
# user = input("Ans: ").strip().lower()
# if user == "a":
#     print("correct")
# else:
#     print("Wrong")


text = "how are you doing" # ["H", "o", "w", " ", "a"...]
# print(text[-1]) 
# slice
# print(text[0:4]) 
# print(text[8:11])

# text[0] = "h" #error
# print(text.lower())
# print(text.capitalize())
# print(text.title())

# print(len(text))
# print(len(text.strip()))

# text = text.strip("!@%$")

# text = text.replace("!","")
# text = text.replace("@","")
# text = text.replace(" ","")
# print(text)

# slug creator
# product = "Kukuli Alata Yeriri"
# slug = product.lower().replace(" ", "-")
# print(slug)

# print(text.startswith("H"))
# print(text.endswith("H"))

# splited = text.split()
# print(splited)

# print(" + ".join(splited))

# Class work
# build a word counter


# print(text.find("area"))
# print(text.index("o", 2, 10))


# special character
# \t - tab
# \n - next line
# \r - return 
# \b - backspace
#  \ - escape character

# print("How are \tyou")
# print("How are \nyou")
# print("How are \b\byou")
# print("How are \\byou")

# print(r"C:\Users\Welcome\OneDrive\Desktop\general\opay-page\index.html")


# Python collection or array
# 1. List [] or list() : Ordered, mutable/changeable, can be indexed and allows duplicate value

garage = ['Tesla', "benz", "Escalade", "Ferrari", "Benz"]
# print(len(garage))
# print(garage[-2])
# print(garage[0:2])

# garage[-1] = "Bugatti"

# garage.reverse()
# print(garage[::-1])

# garage.append("Bugatti")
# garage.extend(["Bugatti", "Toyota"])
# garage.insert( 1, "Bugatti")

# garage.pop(1)
# garage.remove("Benz")
# print(garage.count("Benz"))
# print(garage.index("Benz"))

# gar = garage.copy()

# garage.pop()
# print(garage)
# print(gar)

# garage.sort(key=str.lower, reverse=True)

# print(garage)

# 2. Tuple () or tuple(): ordered, can be indexed, immutable/unchangeable, allows duplicate
garage = ('Tesla', "benz", "Escalade", "Ferrari", "Benz")
# print(garage[0:3])
# print(type(garage))

# garage[0] = "Bugatti"
# garage = list(garage)
# garage[0] = "Bugatti"
# garage = tuple(garage)
# print(garage)

# unpacking
# a, b, c, d, e = garage
# *a, = garage
# *a, b = garage
# c, *a, b = garage
# *a, b, c = garage
# print(c)

# print(garage.count("Benz"))
# print(garage.index("Tesla"))


score = [23, 45, 33, 50]
# print(sum(score))
# print(min(score))
# print(max(score))

# avg = sum(score)/len(score)
# print(avg)


# Python Loop.
# 1. For loop: iterate over a sequence type e.g tuple, list, range, string, set, dict

# name = "Ayomide"
# for letter in name:
#     print(letter)
#     print("____")

# for car in garage:
#     print(f"I own a {car}")

# for i in range(10):
#     print(i)


# 2. while loop: iteration based on a condition
# balance = 100
# while balance > 0:
#     balance -= 10
#     print("Give me the money ehh.. Balance:", balance)

# x = 0
# while x < 10:
#     x += 1
#     print(x)
    

# ticket = 10
# while ticket > 0:
#     age = int(input("Age: "))
#     if age < 18:
#         print("Come back when you are 18")
#         continue
    
#     if ticket < 5:
#         print("No more ticket")
#         break
    
        
#     print("Oya come in...")
#     ticket -= 1
#     print("Ticket:", ticket)
    

# todo app 
database = []
print("Welcome to myTodo app")
while True:
    print("""
        1. Add todo
        2. View todo
        3. Edit todo
        4. Delete todo
        #. Exit    
    """)
    
    choice = input("Choice: ").strip()
    if choice == "1":
        todo = input("Todo: ").strip().capitalize()
        if not todo:
            print("Todo can not be empty!")
            continue
        
        database.append(todo)
        print("Todo Added..")
        
    elif choice == "2":
        if not database:
            print("No todo added!")
            continue
        
        no = 1
        for item in database:
            print(f"{no}. {item}")
            no += 1
    
    elif choice == "#":
        print("Bye..")
        break


# 3. Set
# 4. Dictionary
