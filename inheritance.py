# import backend
from backend import genrate_account_no, BankBackend as BK


class BankFrontend(BK):
    
    def home(self):
        print("""
        1. SIGN IN
        2. REGISTER
        #. EXIT      
              
        """)
        
        choice = input("Choice: ")
        if choice == "1":
            self.signin()
        elif choice == "2":
            self.register()
        elif choice == "3":
            exit()
        else:
            print("Invalid....")
            self.home()
            
        
    def signin(self):
        pass
    
    def register(self):
        fullname = input("Fullname: ").strip().title()
        email = input("Email: ")
        password = input("Password: ")
        res = self.register_user(fullname, email, password)
        print(res)
        self.home()
            

    def menu(self):
        print("""
        1. Deposit
        2. Withdraw
        3. Check balance
        #. exit      
        """)
        
        choice = input("Choice: ")
        if choice == "1":
            self.deposit()
        elif choice == "2":
            self.withdraw()
        elif choice == "3":
            self.check_balance()
        elif choice == "#":
            exit()
        else:
            print("You no sabi wetin you dey do")
            self.menu()
    
  
    def check_balance(self):
        print(f"Your balance is {self.get_balance()}")
        self.menu()
        
    def deposit(self):
        amount = float(input("Amount: "))
        res = self.add_to_balance(amount)
        print(res)
        self.menu()
        
    def withdraw(self):
        amount = float(input("Amount: "))
        res = self.remove_from_balance(amount)
        print(res)
        self.menu()
        
bk = BankFrontend()
bk.home()




# scripts: its a single file that a contains a python code.
# modules: is a scripts that contains functions, variables and classes
# libraries: its a combination of two or more modules 
# frameworks: its a combination of two or more libraries of a particular programming language that streamlines to worklow of a concept/area e.g django (web framework for python), tensorflow/ keras (AI models), Scikit-learn (Machine Models )

