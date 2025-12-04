# Function notes

- Multiple arguments can be passed to functions using ***args**

```python
def add(*args):
    total = 0
    for num in args:
        total += num
    return total
print(add(1, 2, 3, 4, 5))  # Output: 15
```

- keyword arguments can be used to pass arguments in any order

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=21, major="Physics", student_id="S12345") # Output:
# name: Alice
# age: 21
# major: Physics
# student_id: S12345
```
