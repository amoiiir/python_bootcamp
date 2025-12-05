# class Person:

#     species = "Homo sapiens"  # Class attribute

#     # Create constructor
#     def __init__(self, name, age):
#         #Instance attributes
#         self.name = name
#         self.age = age

#     # Instance of a class method
#     def introduce(self):
#         return f"Hi, My name is {self.name} and I'm {self.age} years old."
    
#     # Instance of a class method
#     def have_birthday(self):
#         self.age += 1
#         return f"Happy birthday {self.name} is now {self.age} years old!"
    

# # Creating an object (instance) of the Person class
# person1 = Person("Alice", 30)
# person2 = Person("Bob", 25)

# # Using methods of the Person class
# print(person1.introduce())  # Output: Hi, My name is Alice and I'm 30 years old.
# print(person2.introduce())  # Output: Hi, My name is Bob and I'm 25 years old.

# print(person1.have_birthday())  # Output: Happy birthday Alice is now 31 years old!
# print(person2.have_birthday())  # Output: Happy birthday Bob is now 26 years

# # Accessing class attribute
# print(Person.species)  # Output: Homo sapiens
# print(f"{person1.name} belongs to species {person1.species}.")  # Output: Alice belongs to species Homo sapiens


# # Bank Account
# class BankAccount:
    
#     #Define constructor
#     def __init__(self, account_number, owner, balance = 0):
#         self.account_number = account_number
#         self.owner = owner
#         self.balance = balance
#         self.transaction_history = []

#     # Instance of a class
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount 
#             self.transaction_history.append(f"Deposited ${amount}")
#             return f"Deposited ${amount}. New balance: ${self.balance}"
#         else:
#             return "Invalid deposit amount"
        
#     def withdraw(self, amount):
#         if amount > 0 and amount < self.balance:
#             self.balance -= amount
#             self.transaction_history.append(f"Withdrew ${amount}")
#             return f"Withdrew ${amount}. New balance: ${self.balance}"
#         else:
#             return "Invalid withdrawal amount"

#     def get_balance(self):
#         return f"Owner name: {self.owner}. Current balance: ${self.balance}"

#     def get_transaction_history(self):
#         return f"Transaction History: {self.transaction_history}"

# # Example usage:
# account_num = input("Enter your account number: ")
# account_owner = input("Enter your name: ")
# account_balance = float(input("Enter your initial balance: "))

# acc1 = BankAccount(account_num, account_owner, account_balance)

# print(acc1.get_balance())
# print(acc1.deposit(500))

# Exercose create a simple game chracter class with attributes like health, attack and heal methods

class GameCharacter:

    # create constructor
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    
    def char_info(self):
        return print(f"Your character is {self.name}, current health is {self.health}")

    
    def attack(self, punch, kick):
        if punch:
            self.health -= 10
        elif kick:
            self.health -= 15
        else:
            self.health -= 20
        return f"Your current health is {self.health}"
    
    def heal(self, potion):
        if potion:
            self.health += 20
        return f"Your new health is {self.health}"
    

char1 = GameCharacter("Boras", 130)

print(char1.char_info())
print(char1.attack(punch=False, kick=False))
    



 