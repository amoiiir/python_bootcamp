# def greet_with_title(name, title="Mr. "):
#     return f"Hello, {title}{name}"

# user_input = input("Enter your name: ")

# print(greet_with_title(user_input))

# # kwargs
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name="Alice", age=21, major="Physics", student_id="S12345")

# # flexible arguments
# def flexible_function(*args, **kwargs):
#     print("Positional arguments:")
#     for arg in args:
#         print(arg)
#     print("Keyword arguments:")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# flexible_function(1, 2, 3, name="Bob", age=25)


# # Exercise
# def is_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 return print(f"{num} is not a prime number")
#         return print(f"{num} is a prime number")
#     print(f"{num} is not a valid number")    
    
# test_num = int(input("Enter a number:"))
# is_prime(test_num)

# temperature converter
def temp_farenheit(num):
    return (num * 9/5) + 32

print(temp_farenheit(32))

farenheit = lambda x: (x* 9/5) + 32
print(farenheit(32))
