# Exercise 3

# name = input("Please enter your name: ")
# height = float(input("Enter your height: "))

# while True:
#     try:
#         age = float(input("Enter your age: "))
#         test = float(input("Please enter anything to continue: "))
#         if age > 0:
#             break
#         else:
#             print("Please enter a valid age")
#     # this will get error if the input mismatched with the data type
#     except ValueError: 
#         print("Please enter a valid number!")

# print(f"Hello {name} !")
# print(f"Your age is {age} years old and your height is {height}")


# # Question 1
# first_num = float(input("Please enter the first number: "))
# sec_num = float(input("Please enter the second number: "))

# # Check for valid operation
# while True:
#     try:
#         operation = input("Please enter the operation: ")
#         if operation == '+':
#             result = first_num + sec_num
#             print(f"The sum is {first_num} + {sec_num}: {result}")
#             break
#         elif operation == '-':
#             result = first_num - sec_num
#             print(f"The subtration for {first_num} - {sec_num} is: {result}")
#             break
#         elif operation == '*':
#             result = first_num * sec_num
#             print(f"The multiplication for {first_num} * {sec_num} is: {result}")
#             break
#         else:
#             result = first_num / sec_num
#             print(f"The division for {first_num} / {sec_num} is: {result}")
#             break
#     except ValueError:
#         print("Please enter a valid operation!")

# Question 3 - simple quiz
score = 0
print("What is the national language for Malaysian?")
first_ans = input("a. Bahasa Melayu \nb. Bahasa Inggeris\n")

print("Who is the 10th prime minister of Malaysia?")
second_ans = input("a. Anwar \nb. Not Anwar\n")

print("What is the national food for Malaysian?")
third_ans = input("a. Nasi Lemak \nb. Not Nasi lemak\n")

if(first_ans == 'a'):
    score += 1
if(second_ans == 'a'):
    score += 1
if (third_ans == 'a'):
    score += 1

print(f"Your final score is: {score}/3")









