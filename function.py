# You do something repeatedly - Function
# 1. declaration stage
# 2. Definition stage
# 3. invokation stage


def run():
    print("I am running...")
    
# run()


def area_of_circle():
    pi = 3.142
    r = float(input("Radius(cm): "))
    res = pi * (r**2)
    print(f"Result: {res}cm^2")
    
# area_of_circle()


def cm_to_m():
    val = float(input("Value (cm): "))
    to_m = val/100
    print(f"Ans: {to_m}m")
    
# cm_to_m()


# return function 

def get5():
    return 5

# print(get5())
res = get5()
# print(res)


def get_initials():
    firstname = input("Firstname: ").strip().capitalize()
    lastname = input("Lastname: ").strip().capitalize()
    initials = firstname[0]+lastname[0]
    return initials


# res = get_initials()
# print(res)



# parametized and Non-parametized

def add5(value):
    return value + 5    

# print(add5(6))

def addition(val1, val2, val3=0):
          
    return val1 + val2 + val3


# res = addition(3, 2)
# print(res)


# global and local variable


val = 5

def add10():
    global my_val, val
    
    my_val = 10
    # print(val + my_val)
    
    val += 10
    val = val + 10
    print(val)

def sub10():
    print(val - my_val) 


# add10()
# sub10()

database = [
    {
        "fullname": "TOlulope",
        "email": "tolu@gmail.com",
        "password": "1234"
    },
    {
        "fullname": "TOlulope",
        "email": "tolu@gmail.com",
        "password": "1234"
    }
]

bal = 0

def home():
    
    print("""
    Welcome to MyBank
    
    1. Deposit
    2. Withdraw
    3. Check Balance
    #. Exit       
    """)
    
    choice = input("Choice: ")
    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        check_balance()
    elif choice == "#":
        exit("Goodbye..!")
    else:
        print("Invalid input. Try again")
        home()


def deposit():
    global bal
    
    amount = float(input("Amount: "))
    if amount < 1:
        print("Amount can not be less than 1")
    else:
        bal += amount
        print("Your new balance is:", bal)
        
    home()
    
def withdraw():
    global bal
    
    amount = float(input("Amount: "))
    if amount < 1:
        print("Amount can not be less than 1")
    elif amount > bal:
        print("Insuffucient funds")
    else:
        bal -= amount
        print("Your new balance is:", bal)
        
    home()
    
def check_balance():
    print("Your new balance is:", bal)
    home()
    
    
home()
    
    
# class 
# 1. Write a function that checks if a word is a palindrome e.g MUM
# 2. Convert your todo app to a functional programming approach




# OOP - Object Oriented programming
# object - a properties + functions
# class - a blueprint of an object. an object is an instance of a class
# self - it is used for refrencing

# 1. Write a reusable code
# 2. Modularized

class Todo:
    # properties / attributes
    app_name = "Best TodoApp"
    
    def home(self):
        print(f"Helloo Welcome to {self.app_name}")
        print("""
            1. Add Todo
            2. View Todo      
            #. Exit
        """)
        choice = input("Choice: ")
        if choice == "1":
           self.add_todo()
        elif choice == "2":
            self.view_todo()
        elif choice == "#":
            exit("Goodbye!")
        else:
            print("Invalid Option") 
            
        self.home()
    
    def add_todo(self):
        print("add todo")
        
    def view_todo(self):
        print("view todo")
    

mytodo = Todo()
feranmi_todo = Todo()



# feranmi_todo.app_name = "Feranmi's Todo"
# print(mytodo.app_name)
# print(feranmi_todo.app_name)

# mytodo.home()