from BankAccount import BankAccount
import random

# Dictionary to store all accounts: {acc_num: BankAccount}
accounts = {}

# Track currently logged-in account
current_account = None
current_acc_num = None

def generate_unique_account_number():
    """Generate a unique 6-digit account number."""
    while True:
        acc_num = str(random.randint(100000, 999999))
        if acc_num not in accounts:
            return acc_num

def create_account():
    """Create a new account."""
    global current_account, current_acc_num
    
    acc_num = generate_unique_account_number()
    acc_name = input("Please enter your name: ")
    
    # Create account and store in dictionary
    accounts[acc_num] = BankAccount(acc_num, acc_name)
    current_account = accounts[acc_num]
    current_acc_num = acc_num
    
    print(f"\nAccount created successfully!")
    print(f"Your account number: {acc_num}")
    print(accounts[acc_num].acc_information())
    print("You are now logged in.\n")

def login():
    """Login to an existing account."""
    global current_account, current_acc_num
    
    acc_num = input("Please enter your account number: ")
    
    if acc_num in accounts:
        current_account = accounts[acc_num]
        current_acc_num = acc_num
        print(f"\nWelcome back, {current_account.acc_owner}!")
        print(current_account.acc_information())
        print()
    else:
        print("\nAccount not found. Please check your account number.\n")

def logout():
    """Logout from current account."""
    global current_account, current_acc_num
    
    if current_account is None:
        print("\nNo account logged in.\n")
    else:
        print(f"\nThank you for banking with us, {current_account.acc_owner}!")
        current_account = None
        current_acc_num = None
        print()

def is_logged_in():
    """Check if user is logged in."""
    if current_account is None:
        print("\nPlease login or create an account first.\n")
        return False
    return True

# Main program
print("******************************************************************************************")
while True:
    print("Welcome to Bank Nasional!\n\nPlease select an option:")
    print("1. Create account")
    print("2. Login")
    print("3. Check your balance")
    print("4. Deposit money")
    print("5. Withdraw money")
    print("6. Check transaction history")
    print("7. Logout")
    print("8. Exit")
    
    option = int(input("\nYour selection: "))

    if option == 1:
        create_account()
    
    elif option == 2:
        login()
    
    elif option == 3:
        if is_logged_in():
            print(current_account.get_balance())
            print()
    
    elif option == 4:
        if is_logged_in():
            amount = float(input("Please enter amount to deposit: "))
            print(current_account.deposit(amount))
            print()
    
    elif option == 5:
        if is_logged_in():
            amount = float(input("Please enter amount to withdraw: "))
            print(current_account.withdraw(amount))
            print()
    
    elif option == 6:
        if is_logged_in():
            print(current_account.get_transaction())
            print()
    
    elif option == 7:
        logout()
    
    elif option == 8:
        if current_account is not None:
            logout()
        print("Thank you for banking with us!")
        break
    
    else:
        print("\nInvalid option selected. Please try again.\n")
    
    print("******************************************************************************************")