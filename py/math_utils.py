def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

PI = 3.142

class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    def __init__(self):
        self.history = []

    def calculate(self, operation, a, b):
        """Perform the given operation on a and b and store the result in history."""
        if operation == 'add':
            result = add(a, b)
        elif operation == 'subtract':
            result = subtract(a, b)
        elif operation == 'multiply':
            result = multiply(a, b)
        elif operation == 'divide':
            result = divide(a, b)
        else:
            raise ValueError("Unsupported operation.")
        
        self.history.append((operation, a, b, result))
        return result