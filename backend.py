import random as rd, math, time, datetime as dt
import pyttsx3


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
        
        

def genrate_account_no():
    # random. 
    pass

# gen = int(rd.random() * 10000000000 // 1)
# gen = rd.random() * 10000000000
# print(math.floor(gen))


# gen = rd.randint(10000000000, 19999999999)

cars = ['toyota', 'benz', 'nissan']
# print(rd.choice(cars))
# print(rd.choices(cars, k=2))

# print(gen)
    
# print("Loading...")
# time.sleep(3)
# print("done")

# print(dt.datetime.now())


# pyttsx3.speak("Yo! How are you doing today?")

engine = pyttsx3.init()
engine.say("Yo! How are you doing today?")
voices = engine.getProperty('voices')       # getting details of current voice
# engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   
# engine.runAndWait()
# engine.stop()

# print(voices[1].id)

