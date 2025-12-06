from BankAccount import BankAccount
import uuid
import random

# create variable
acc_num = input("Please enter account number: ")
acc_name = input("Please enter your name: ")

acc1 = BankAccount(acc_num, acc_name)

print("******************************************************************************************")
while True:
    print("Welcome to Bank nasional!\n\nPlease select your service today:")
    option = int(input("1. Check your balance.\n2. Deposit money\n3. Withdraw money\n4. Check transaction history\n5. Exit\nYour selection: "))

    if option == 1:
        print(acc1.get_balance())
    elif option == 2:
        amount = float(input("Please enter amount: "))
        print(acc1.deposit(amount))
    elif option == 3:
        amount = float(input("Please enter amount: "))
        print(acc1.withdraw(amount))
    elif option == 4:
        print(acc1.get_transaction())
    elif option == 5:
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid option selected. Please try again.")
    print("******************************************************************************************")


