

class BankBackend:
    __balance = 0
    
    __db = []
    
    
    def register_user(self, fullname, email, password):
        if not fullname or not email or not password:
            return "All fields are required."
        
        else:
            for data in self.__db:
                if data["email"] == email:
                    return "Email already exist"
            
            user = {
                "fullname": fullname,
                "email": email,
                "password": password,
                "balance": 0.0
            }
            self.__db.append(user)
            print(self.__db)
            return "Account created successfully"
            
        
    

    def get_balance(self):
        return self.__balance
        
    
    def add_to_balance(self, amount):
        if amount < 1:
            return "Amount can't be less that #1"
        else:
            self.__balance += amount
            return f"Deposit successfull. Your new balance is #{self.__balance}"
        
        
    def remove_from_balance(self, amount):
        if amount < 1:
            return "Amount can't be less that #1"
        elif amount > self.__balance:
            return "Insufficient Fund"
        else:
            self.__balance -= amount
            return f"Withdrawal successfull. Your new balance is #{self.__balance}"




class BankFrontend(BankBackend):
    
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