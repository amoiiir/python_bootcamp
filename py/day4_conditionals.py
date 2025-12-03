# Write  a  program  that  categorizes  BMI  (Body  Mass  Index)  intounderweight(<18.5),  normal  weight(<24.9),  overweight(<29.9),  and
# obesity(<30.0). (formula = kg/m^2)

weight = float(input("Please enter your weight (in kg): "))
height = float(input("Please enter your height (in cm): "))

bmi = weight / (height / 100) ** 2

if bmi < 18.5:
    print(f"Your weight is {bmi}. You are underweight.")
elif 18.5 <= bmi < 24.9:
    print(f"Your weight is {bmi}. You have a normal weight.")  
elif 25 <= bmi < 29.9:
    print(f"Your weight is {bmi}. You are overweight.")
elif bmi >= 30:
    print(f"Your weight is {bmi}. You are obese.")



