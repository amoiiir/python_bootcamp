name = 'Nick' # string
age = 30 # integer
weight = 70.5 # float
is_female = False # boolean

print(name)
print(type(name))
print(age)
print(type(age))
print(weight)
print(type(weight))
print(is_female)
print(type(is_female))

print("Hello, " + name + "! You are " + str(age) + " years old." + " Your weight is " + str(weight) + " kg." + " You are female: " + str(is_female) + ".")
print(type(name))

# Math operations
x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y) # floor division
print(x // y) # integer division
print(x % y) # modulus (remainder)
print(x ** y) # exponentiation  


# convert celcius to fahrenheit
celcius = 25

farenheit = (celcius * 9/5) + 32
print("The temperature is " + str(farenheit) + "°F")