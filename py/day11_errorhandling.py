# get user age

# def validate_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     if age > 150:
#         raise ValueError("Age is not realsitic")
    
# try:
#     validate_age(-130)
# except ValueError as e:
#     print(f"Validation error: {e}")

# #Basic excpetion handling
# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(f"Result: {result}")
# except ValueError:
#     print("Invalid input! Please enter a number")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# using finally
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found!")
else:
    content = file.read()
    print(content)
# Finally block will always execute
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed.")
    print("Cleanup done.")