# while loop used when we need conditional looping
# for loop used when we need to iterate

# for m in range(0,10,3):
#     print(m)


# # Multiplication table
# num = int(input("Please enter your number(1-12): "))

# if num > 12 or num < 1:
#     print("Please enter a valid number between 1 to 12")
# else:
#     print(f"You choosed multiplication of: {num}")
#     for i in range(1, 13):
#         result = num * i
#         print(f"{i} x {num} = {result}")

# get all prime numbers within the limit of 20

for i in range(0,20):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)

