# Initialize bank account class

class BankAccount:

    # Define constructor
    def __init__(self, acc_num, acc_owner, acc_balance = 0):
        self.acc_num = acc_num
        self.acc_owner = acc_owner
        self.acc_balance = acc_balance
        self.transaction_history = []

    def acc_information(self):
        return f"Welcome {self.acc_owner}! Your current balance is {self.acc_balance} and your account number is {self.acc_num}"

    def deposit(self, amount):
        if amount > 0:
            self.acc_balance = self.acc_balance + amount
            self.transaction_history.append(f"Deposited amount RM{amount}")
            return f"Your new account balance is: {self.acc_balance}"
        else:
            return f"You input an invalid amount of RM {amount}"
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.acc_balance:
            self.acc_balance -= amount
            self.transaction_history.append(f"Withdrew RM{amount}")
            return f"Withdrew RM{amount}. New balance: RM{self.acc_balance}"
        else:
            return "Invalid withdrawal amount or insufficient balance"
        
    def get_transaction(self):
        return f"Transaction history: {self.transaction_history}"
    
    def get_balance(self):
        return f"Current balance is: {self.acc_balance}"

