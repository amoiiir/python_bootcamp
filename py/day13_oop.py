# Inheritance

class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
        return 0
    
class Circle(Shape):

    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.142 * self.radius * self.radius
    
class Rectangle(Shape):

    def __init__(self, width, length):
        super().__init__("Rectangle")
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    
# Both Rectangle and Circle inherit 'name' attribute from Shape
circle = Circle(5)
print(f"{circle.name} area: {circle.area()}")  # Output: Circle area: 78.53975

rectangle = Rectangle(4, 6)
print(f"{rectangle.name} area: {rectangle.area()}")  # Output: Rectangle area: 24

# Polymorphism

def print_area(shape):
    print(f"{shape.name} area: {shape.area()}")

# Same method call, different behaviors
print_area(circle)
print_area(rectangle)

# # Or with a list
# shapes = [Circle(3), Rectangle(5, 3)]

# for shape in shapes:
#     print_area(shape)